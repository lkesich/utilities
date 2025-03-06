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

class TestFlattenNestedList(unittest.TestCase):
    def test_one_level_list(self):
        result = core.flatten_nested_list(['a','b',['c']])
        self.assertEqual(result, ['a', 'b', 'c'])

    def test_multi_level_list(self):
        result = core.flatten_nested_list([1, [2], [[3], 4]])
        self.assertEqual(result, [1, 2, 3, 4])

    def test_mixed_type_list(self):
        result = core.flatten_nested_list([None, [[False]], [1], 'a'])
        self.assertEqual(result, [None, False, 1, 'a'])

if __name__ == '__main__':
    unittest.main()