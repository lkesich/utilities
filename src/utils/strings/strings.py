__docformat__ = 'google'

__all__ = [
    'replace_all',
    'find',
    'squish',
    'normalize_whitespace',
    'check_case',
    'proper_case',
    'match_case'
]

from typing import List, Pattern
import re

def replace_all(replacements: dict, text: str) -> str:
    """Perform multiple replacements in a text string.
    
    Args:
        replacements: Dictionary mapping patterns (string or regex) to replacements
        text: String to perform replacements on
        
    Returns:
        String with all replacements applied
        
    Examples:
        >>> replace_all({'a': 'd', 'b': 'e'}, 'abc')
        'dec'
        >>> replace_all({r'\d+': '#'}, 'a1')
        'a#'
    """
    if len(replacements) > 0:
        for (old_pattern, new_pattern) in replacements.items():
            text = re.sub(old_pattern, new_pattern, text)
    return text

def find(pattern: re.Pattern | str, text: str) -> str:
    """Get first matching substring from a string.
        
    Returns:
        First match for pattern in text

    Examples:
        >>> find('\\d+', 'a 1 b 2')
        '1'
        >>> find(re.compile('\\d+'), 'a 1 b 2')
        '1'
    """
    if not isinstance(text, str):
        raise TypeError('Input text must be a string')
    elif not isinstance(pattern, re.Pattern | str):
        raise TypeError('Pattern must be a string or re.compile object')
    else:
        match = re.search(pattern, text)
        return match.group(0) if match is not None else None

def squish(text: str) -> str:
    """Normalize whitespace in a string.
    
    Trim whitespace at the start and end of a text string; replace all internal
    whitespace with a single space.
    
    Args:
        text: String to normalize
        
    Returns:
        String with normalized whitespace
        
    Examples:
        >>> squish("  hello   world  ")
        'hello world'
    """
    return re.sub(r'\s+', ' ', text.strip())

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace and punctuation spacing in text.
    
    This function performs several whitespace normalization operations:
      1. Trims whitespace from start and end of string
      2. Applies `squish` to replace all internal whitespace with a single space
      3. Removes unnecessary whitespace around punctuation using `replace_all`
      4. Adds whitespace around punctuation when necessary using `replace_all`
    
    Args:
        text: String to standardize
    
    Returns:
        String with normalized whitespace
    
    Note:
        See the function implementation for punctuation spacing rules.
    
    Examples:
        >>> normalize_whitespace(" a ,b c( 1 ) ")
        'a, b c (1)'
    """
    # Characters that should not have leading whitespace
    _remove_leading_space = ['.', ',', ':', ';', ')', '!', '?', '/', '-']
    # Characters that should not have trailing whitespace
    _remove_trailing_space = ['(', '/', '-']
    # Characters that should have leading whitespace
    _add_leading_space = ['&', '(']
    # Characters that should have trailing whitespace
    _add_trailing_space = ['&', ')', ',', '.', ':', ';', '!', '?']

    replacements = {
        f"\s([{''.join(_remove_leading_space)}])": r"\g<1>"
        , f"([{''.join(_remove_trailing_space)}])\s": r"\g<1>"
        , f"(?<=[^\s])([{''.join(_add_leading_space)}])": r" \g<1>"
        , f"([{''.join(_add_trailing_space)}])(?=[^\s])": r"\g<1> "
    }
    return replace_all(replacements, squish(text))

def check_case(text: str) -> str:
    """Check if a string is upper, lower, or mixed case.

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
    """
    if type(text) != str:
        raise TypeError('Input must be a string')
    elif text.isupper():
        return 'upper'
    elif text.islower():
        return 'lower'
    else:
        return 'mixed'

def proper_case(text: str) -> str:
    """Apply proper case to a string.

    The rules for proper case are as follows:
      1. Apply title case (all words in string capitalized)
      2. Lowercase conjunctions and other words that are commonly lowercase
      3. Capitalize the first word in the string, even if it is commonly lowercase

    Args:
        text: String to proper case
        
    Returns:
        Proper cased string
        
    Raises:
        TypeError: If input is not a string

    Examples:
        >>> proper_case('of mice and men')
        'Of Mice and Men'
    """
    _ALWAYS_LOWERCASE = ['of', 'and', 'for']
    title = text.title()
    
    for word in _ALWAYS_LOWERCASE:
        title = re.sub(f'(?i)(?<=\s){word}\\b', word, title)
    return title

def match_case(text: str, match_reference: str) -> str:
    """Align the case of string with the case of comparison string.
    
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
    """
    if {type(text), type(match_reference)} != {str}:
        raise TypeError('Both inputs must be strings')
    elif check_case(text) == check_case(match_reference):
        return text
    elif match_reference.isupper():
        return text.upper()
    elif match_reference.islower():
        return text.lower()
    else:
        return proper_case(text)

