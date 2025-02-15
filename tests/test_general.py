import unittest
from src.utils import general

class TestChainOperations(unittest.TestCase):
    def test_chain_operations(self):
        result = general.chain_operations(' abc ', [str.upper, str.strip])
        self.assertEqual(result, 'ABC')

if __name__ == '__main__':
    unittest.main()