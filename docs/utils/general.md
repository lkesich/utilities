Module utils.general
====================
General utility operations for creating cleaner, more readable code.

Functions
---------

`chain_operations(arg, order_of_operations: List[Callable])`
:   Apply multiple functions to an argument in sequence.
    
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