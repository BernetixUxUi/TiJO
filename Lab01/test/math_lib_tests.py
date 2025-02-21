import unittest
from ..src.math_lib import find_max, is_perfect


class TestMathLib(unittest.TestCase):

    # Testy dla max()
    def test_none_input(self):
        self.assertIsNone(find_max(None))

    def test_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_single_element(self):
        self.assertEqual(find_max([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(find_max([1, 3, 7, 2]), 7)

    # Testy dla is_perfect()
    def test_negative_number(self):
        self.assertFalse(is_perfect(-6))

    def test_zero(self):
        self.assertFalse(is_perfect(0))

    def test_non_perfect_number(self):
        self.assertFalse(is_perfect(10))

    def test_perfect_number(self):
        self.assertTrue(is_perfect(6))

    def test_another_perfect_number(self):
        self.assertTrue(is_perfect(28))


if __name__ == "__main__":
    unittest.main()