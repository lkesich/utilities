Module utils.strings
====================
String manipulation utilities for text processing.

This module provides functions for standardizing text formatting,
manipulating case, creating identifiers, and performing text replacements.

Functions
---------

`check_case(text: str) ‑> str`
:   Check if a string is upper, lower, or mixed case.
    
    Args:
        text: String to check
        
    Returns:
        'upper', 'lower', or 'mixed'
        
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> check_case('of Mice and Men')
        'mixed'
        >>> check_case('of mice and men')
        'lower'

`create_surrogate_key(fields: List, delimiter='_') ‑> str`
:   Create surrogate primary key from a list.
    
    Args:
        fields: List of elements to include
        delimiter: String delimiter. Defaults to _
    
    Returns:
        Surrogate primary key
    
    Examples:
        >>> create_surrogate_key([12, 'a.b', None, 'c d'])
        '12_ab_cd'
        >>> create_surrogate_key([12, 'a.b', None, 'c d'], '~')
        '12~ab~cd'

`match_case(text: str, match_reference: str) ‑> str`
:   Align the case of string with the case of comparison string.
    
    Args:
        text: String to normalize case
        match_reference: String to reference for case
        
    Returns:
        String with matched case applied
        
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> match_case('AbCd', 'a')
        'abcd'

`normalize_whitespace(text: str) ‑> str`
:   Normalize whitespace and punctuation spacing in text.
    
    This function performs several whitespace normalization operations:
      1. Trims whitespace from start and end of string
      2. Replaces all internal whitespace characters with a single space
      3. Removes unnecessary whitespace around punctuation
      4. Adds whitespace around punctuation when necessary
    
    Args:
        text: String to standardize
    
    Returns:
        String with normalized whitespace
    
    Note:
        See the function implementation for punctuation spacing rules.
    
    Examples:
        >>> normalize_whitespace(" a ,b c( 1 ) ")
        'a, b c (1)'

`proper_case(text: str) ‑> str`
:   Apply proper case to a string.
    
    The rules for proper case are as follows:
      1. Apply title case (all words in string capitalized)
      2. Lowercase conjunctions and other words that are commonly lowercase
      3. Capitalize the first word in the string, even if it is commonly lowercase
    
    Args:
        text: String to apply proper case
        
    Returns:
        Proper cased string
        
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> proper_case('of mice and men')
        'Of Mice and Men'

`replace_all(replacements: dict, text: str) ‑> str`
:   Perform multiple replacements in a text string.
    
    Args:
        replacements: Dictionary mapping patterns (string or regex) to replacements
        text: String to perform replacements on
        
    Returns:
        String with all replacements applied
        
    Examples:
        >>> replace_all({'a': 'A'}, 'abc')
        'Abc'
        >>> replace_all({r'\d+': '#'}, 'a1')
        'a#'

`squish(text: str) ‑> str`
:   Normalize whitespace in a string.
    
    Trim whitespace at the start and end of a text string; replace all internal
    whitespace with a single space.
    
    Args:
        text: String to normalize
        
    Returns:
        String with normalized whitespace
        
    Examples:
        >>> squish("  hello   world  ")
        'hello world'