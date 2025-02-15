import unittest
from src.utils import strings

class TestStringSquish(unittest.TestCase):
    def test_string_squish(self):
        result = strings.string_squish(' a b  c ')
        self.assertEqual(result, 'a b c')

class TestStandardizeWhitespace(unittest.TestCase):
    def test_remove_trailing_whitespace(self):
        result = strings.standardize_whitespace('( ab)')
        self.assertEqual(result, '(ab)')

    def test_add_trailing_whitespace(self):
        result = strings.standardize_whitespace('a,b')
        self.assertEqual(result, 'a, b')

    def test_remove_leading_whitespace(self):
        result = strings.standardize_whitespace(' a /b ')
        self.assertEqual(result, 'a/b')

    def test_add_leading_whitespace(self):
        result = strings.standardize_whitespace('a& b')
        self.assertEqual(result, 'a & b')

    def test_multiple_conditions(self):
        result = strings.standardize_whitespace(' a ,b c( 1 ) d&e -- f g /h .')
        self.assertEqual(result, 'a, b c (1) d & e--f g/h.')

class TestReplaceAll(unittest.TestCase):
    def test_replace_all_text(self):
        result = strings.replace_all({'a':'A','A':'b'}, 'ab')
        self.assertEqual(result, 'bb')

    def test_replace_all_regex(self):
        result = strings.replace_all({'&(\w+)':'\g<1>'}, 'aa&bb')
        self.assertEqual(result, 'aabb')

class TestCreateSurrogateKey(unittest.TestCase):
    def test_create_surrogate_key(self):
        result = strings.create_surrogate_key([12, 'a.b', None, 'c d'])
        self.assertEqual(result, '12_ab_cd')

    def test_create_surrogate_key_custom_delimiter(self):
        result = strings.create_surrogate_key([12, 'a.b', None, 'c d'], '~')
        self.assertEqual(result, '12~ab~cd')

class TestCheckCase(unittest.TestCase):
    def test_check_case_upper(self):
        result = strings.check_case('LEPAGE')
        self.assertEqual(result, 'upper')

    def test_check_case_lower(self):
        result = strings.check_case('lepage')
        self.assertEqual(result, 'lower')

    def test_check_case_mixed(self):
        result = strings.check_case('LePage')
        self.assertEqual(result, 'mixed')

    def test_check_case_error(self):
        self.assertRaises(TypeError, strings.check_case, 1)

class TestProperCase(unittest.TestCase):
    def test_proper_case(self):
        result = strings.proper_case('of mice and men')
        self.assertEqual(result, 'Of Mice and Men')

class TestMatchCase(unittest.TestCase):
    def test_match_case_type_error_input(self):
        self.assertRaises(TypeError, strings.match_case, 'a', 1)

    def test_match_case_type_error_match(self):
        self.assertRaises(TypeError, strings.match_case, 1, 'a')
    
    def test_match_case_mixed_to_lower(self):
        result = strings.match_case('of Mice and Men', 'a')
        self.assertEqual(result, 'of mice and men')

    def test_match_case_mixed_to_upper(self):
        result = strings.match_case('of Mice and Men', 'A')
        self.assertEqual(result, 'OF MICE AND MEN')

    def test_match_case_mixed_to_mixed(self):
        result = strings.match_case('of Mice and Men', 'aB')
        self.assertEqual(result, 'of Mice and Men')

    def test_match_case_upper_to_lower(self):
        result = strings.match_case('OF MICE AND MEN', 'a')
        self.assertEqual(result, 'of mice and men')

    def test_match_case_upper_to_upper(self):
        result = strings.match_case('OF MICE AND MEN', 'A')
        self.assertEqual(result, 'OF MICE AND MEN')

    def test_match_case_upper_to_mixed(self):
        result = strings.match_case('OF MICE AND MEN', 'aB')
        self.assertEqual(result, 'Of Mice and Men')

    def test_match_case_lower_to_lower(self):
        result = strings.match_case('of mice and men', 'a')
        self.assertEqual(result, 'of mice and men')

    def test_match_case_lower_to_upper(self):
        result = strings.match_case('of mice and men', 'A')
        self.assertEqual(result, 'OF MICE AND MEN')

    def test_match_case_lower_to_mixed(self):
        result = strings.match_case('of mice and men', 'aB')
        self.assertEqual(result, 'Of Mice and Men')

if __name__ == '__main__':
    unittest.main()