#!/usr/bin/python3
""" Unit test for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class that test max_integer
    """

    def test_empty_list(self):
        """Test for empty list
        """
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test for one element
        """
        self.assertEqual(max_integer([1]), 1)

    def test_two_elements(self):
        """Test for two elements
        """
        self.assertEqual(max_integer([1, 2]), 2)

    def test_three_elements(self):
        """Test for three elements
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_string_elements(self):
        """Test for string elements
        """
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_negative_elements(self):
        """Test for negative elements
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_float_elements(self):
        """Test for float elements
        """
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_long_elements(self):
        """Test for long elements
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_long_negative_elements(self):
        """Test for long negative elements
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5, -6, -7]), -1)

    def doCleanups(self) -> None:
        return super().doCleanups()


if __name__ == '__main__':
    unittest.main()
