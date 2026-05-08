__docformat__ = 'google'

__all__ = [
    'upsert_from_parquet',
    'upsert_from_dataframe'
]

from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import pandas as pd
import pyarrow.parquet
import uuid
from typing import Callable
from pathlib import Path

def _check_distinct_key(
    client: bigquery.Client,
    target_table: str,
    primary_keys: list[str]
):
    query = client.query(
        f"""
        SELECT(SELECT COUNT DISTINCT(*) FROM `{target_table}`) - 
        (SELECT COUNT (*) FROM (
            SELECT DISTINCT {' ,'.join(primary_keys)} FROM `{target_table}`
        )) as difference
        """
    )
    result = query.result()
    if next(result).difference > 0:
        raise ValueError('Primary key is not distinct in target table')

def _upsert(
    load_fn: Callable,
    client: bigquery.Client,
    target_table: str,
    columns: list[str],
    primary_keys: list[str],
    check_distinct: bool = False
):
    staging_table = f'{target_table}_staging_{uuid.uuid4().hex}'
    
    try:
        client.get_table(target_table)

        if check_distinct:
            _check_distinct_key(client, target_table, primary_keys)

        non_key_cols = [col for col in columns if col not in primary_keys]
        merge_condition = '\n\tAND '.join([f't.{col} = s.{col}' for col in primary_keys])
        match_condition = ', '.join([f't.{col} = s.{col}' for col in non_key_cols])

        merge_sql = f"""
            MERGE INTO `{target_table}` AS t
            USING `{staging_table}` AS s
            ON {merge_condition}
            WHEN MATCHED THEN
                UPDATE SET
                    {match_condition}
            WHEN NOT MATCHED THEN
                INSERT ROW
        """

        client.query(merge_sql).result()
    
    except NotFound:
        load_fn(target_table)
    
    finally:
        client.delete_table(staging_table, not_found_ok = True)

def upsert_from_dataframe(
    df: pd.DataFrame,
    client: bigquery.Client,
    target_table: str,
    primary_keys: list[str],
    check_distinct: bool = False
):
    """Upsert to a BigQuery table from a Pandas dataframe.

    Args:
        df: A Pandas dataframe with data to be upserted
        client: A google.bigquery.Client object
        target_table: The BigQery table to be altered
        primary_keys: The unique key or keys to be used for merging
        check_distinct: If True, the target table will be checked for duplicate `primary_keys`
    """
    config = bigquery.LoadJobConfig(
        write_disposition = 'WRITE_TRUNCATE',
        autodetect = True
    )

    columns = df.columns

    def load_fn(table):
        client.load_table_from_dataframe(df, table, job_config = config)
    
    _upsert(
        load_fn = load_fn,
        client = client,
        target_table = target_table,
        columns = columns,
        primary_keys = primary_keys,
        check_distinct = check_distinct
    )

def upsert_from_parquet(
    parquet_path: str | Path,
    client: bigquery.Client,
    target_table: str,
    primary_keys: list[str],
    check_distinct: bool = False
):
    """Upsert to a BigQuery table from a parquet file.

    Args:
        parquet_path: The path of the parquet file to be upserted
        client: A google.bigquery.Client object
        target_table: The BigQery table to be altered
        primary_keys: The unique key or keys to be used for merging
        check_distinct: If True, the target table will be checked for duplicate `primary_keys`
    """
    config = bigquery.LoadJobConfig(
        source_format = 'PARQUET',
        write_disposition = 'WRITE_TRUNCATE',
        autodetect = True
    )

    columns = pyarrow.parquet.read_schema(parquet_path).names

    def load_fn(table):
        with open(parquet_path, 'rb') as file:
            client.load_table_from_file(file, table, job_config = config)

    _upsert(
        load_fn = load_fn,
        client = client,
        target_table = target_table,
        columns = columns,
        primary_keys = primary_keys,
        check_distinct = check_distinct
    )