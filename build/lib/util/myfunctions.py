from typing import List, Callable
from functools import reduce

def chain_operations(arg, order_of_operations: List[Callable]):
    return reduce(lambda x, f: f(x), order_of_operations, arg)
