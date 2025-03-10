__docformat__ = 'google'

__all__ = [
    'chain_operations',
    'create_surrogate_key',
    'flatten_nested_list'
]

from typing import List, Callable, Any
from functools import reduce
from itertools import chain
import re

def chain_operations(arg, order_of_operations: List[Callable]):
    """Apply multiple functions to an argument in sequence.

    This function is an implementation of functools.reduce. It allows functions
    from different classes to be applied to a variable in a specified order,
    without naming the variable each time.
    
    Args:
        arg: Item to apply functions to
        order_of_operations: List of functions to apply in order
        
    Returns:
        Item with all operations applied
        
    Examples:
        >>> chain_operations(' abc ', [str.upper, str.strip])
        'ABC'
    """
    return reduce(lambda x, f: f(x), order_of_operations, arg)

def create_surrogate_key(fields: List, delimiter='_') -> str:
    """Create surrogate primary key from a list of fields.

    Args:
        fields: List of elements to include
        delimiter: String delimiter. Defaults to `_`
    
    Returns:
        Surrogate primary key

    Examples:
        >>> create_surrogate_key([12, 'a.b', None, 'c d'])
        '12_ab_cd'
        >>> create_surrogate_key([12, 'a.b', None, 'c d'], '~')
        '12~ab~cd'
    """
    elements = list(filter(None, fields))
    elements = map(lambda e: re.sub('[^a-zA-Z0-9]', '', str(e)), elements)
    id_string = f'{delimiter}'.join(list(elements))
    return id_string

def flatten_nested_list(items: List[Any|List[Any]]) -> List:
    """Flatten lists with nested elements of arbitrary depths.

    Args:
        items: List to flatten
    
    Returns:
        Flattened list

    Examples:
        >>> flatten_nested_list(['a', ['b'], 'c'])
        ['a','b','c']
        >>> flatten_nested_list([1, [2], [[3], [4]]])
        [1, 2, 3, 4]
    """
    return list(
        chain.from_iterable(
            [item] if not isinstance(item, list)
            else flatten_nested_list(item)
            for item in items
            )
        )
