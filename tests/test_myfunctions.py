import unittest
from src.utils import myfunctions

class TestSimple(unittest.TestCase):
    def test_chain_operations(self):
        result = myfunctions.chain_operations(' abc ', [str.upper, str.trim])
        self.assertEqual(result, 'ABC')

if __name__ == '__main__':
    unittest.main()