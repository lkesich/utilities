from typing import List
import re

def replace_all(replacements: dict, text: str):
    """
    Performs multiple replacements in a text string using a dictionary of old->new values
    Dictionary items can be text or regular expressions
    """
    if len(replacements) > 0:
        for (old_pattern, new_pattern) in replacements.items():
            text = re.sub(old_pattern, new_pattern, text)
    return text

def squish(input_string: str):
    """
    Python equivalent of stringr::str_squish() in R
    Replaces all whitespace with a single space character
    Strips leading and trailing whitespace
    """
    return re.sub(r'\s+', ' ', input_string.strip())

_REMOVE_LEADING_SPACE = ['.', ',', ':', ';', ')', '!', '?', '/', '-']
_REMOVE_TRAILING_SPACE = ['(', '/', '-']
_ADD_LEADING_SPACE = ['&', '(']
_ADD_TRAILING_SPACE = ['&', ')', ',', '.', ':', ';', '!', '?']

def standardize_whitespace(input_string: str):    
    replacements = {
        f"\s([{''.join(_REMOVE_LEADING_SPACE)}])": "\g<1>"
        , f"([{''.join(_REMOVE_TRAILING_SPACE)}])\s": "\g<1>"
        , f"(?<=[^\s])([{''.join(_ADD_LEADING_SPACE)}])": " \g<1>"
        , f"([{''.join(_ADD_TRAILING_SPACE)}])(?=[^\s])": "\g<1> "
    }
    return replace_all(replacements, squish(input_string))

standardize_whitespace.__doc__ = f"""
    Replaces all whitespace with a single space character
    Strips leading whitespace from these characters: {' '.join(_REMOVE_LEADING_SPACE)}
    Strips trailing whitespace from these characters: {' '.join(_REMOVE_TRAILING_SPACE)}
    Adds leading whitespace from these characters: {' '.join(_ADD_LEADING_SPACE)}
    Adds trailing whitespace from these characters: {' '.join(_ADD_TRAILING_SPACE)}
    """

def create_surrogate_key(fields: List, delimiter='_'):
    """
    Convert all elements to strings and concatenates them with delimiter
    Remove all characters that are non-alphanumeric, including whitespace
    """
    elements = list(filter(None, fields))
    elements = map(lambda e: re.sub('[^a-zA-Z0-9]', '', str(e)), elements)
    id_string = f'{delimiter}'.join(list(elements))
    return id_string

def check_case(input_string: str) -> str:
    """
    Check if a string is upper, lower, or mixed case.
    """
    if type(input_string) != str:
        raise TypeError('Input must be a string')
    elif input_string.isupper():
        return 'upper'
    elif input_string.islower():
        return 'lower'
    else:
        return 'mixed'

_ALWAYS_LOWERCASE = ['of', 'and', 'for']

def proper_case(input_string: str) -> str:
    title = input_string.title()
    for word in _ALWAYS_LOWERCASE:
        title = re.sub(f'(?i)(?<=\s){word}\\b', word, title)
    return title

def match_case(input_string: str, match_string: str) -> str:
    """
    Aligns the case of string with the case of comparison string
    Does not modify input string if both strings are mixed case
    """
    if {type(input_string), type(match_string)} != {str}:
        raise TypeError('Both inputs must be strings')
    elif check_case(input_string) == check_case(match_string):
        return input_string
    elif match_string.isupper():
        return input_string.upper()
    elif match_string.islower():
        return input_string.lower()
    else:
        return proper_case(input_string)

