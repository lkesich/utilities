import unittest
from utils.core import core

class TestChainOperations(unittest.TestCase):
    def test_chain_operations(self):
        result = core.chain_operations(' abc ', [str.upper, str.strip])
        self.assertEqual(result, 'ABC')

class TestCreateSurrogateKey(unittest.TestCase):
    def test_create_surrogate_key(self):
        result = core.create_surrogate_key([12, 'a.b', None, 'c d'])
        self.assertEqual(result, '12_ab_cd')

    def test_create_surrogate_key_custom_delimiter(self):
        result = core.create_surrogate_key([12, 'a.b', None, 'c d'], '~')
        self.assertEqual(result, '12~ab~cd')

if __name__ == '__main__':
    unittest.main()