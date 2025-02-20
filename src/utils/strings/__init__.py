"""
String manipulation utility functions for text processing.

This module provides functions for standardizing text formatting,
manipulating case, creating identifiers, and performing text replacements.
"""

from .strings import *

__all__ = [
    'replace_all',
    'squish',
    'normalize_whitespace',
    'create_surrogate_key',
    'check_case',
    'proper_case',
    'match_case'
]