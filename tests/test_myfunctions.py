from util import myfunctions
def test_chain_operations():
    assert myfunctions.chain_operations(
        ' abc ', 
        [str.upper, str.trim]
    ) == 'ABC'