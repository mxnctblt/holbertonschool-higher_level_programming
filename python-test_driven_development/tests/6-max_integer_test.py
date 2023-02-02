#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):



    def test_positives(self):
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [4, 4, 4, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1, 2, 4, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(test_list), 4.4)

        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(max_integer(test_list), 15)

        test_list = [15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14]
        self.assertEqual(max_integer(test_list), 15)


    def test_negatives(self):

        test_list = [-2, 0, 2, 4]
        self.assertEqual(max_integer(test_list), 4)

        test_list = [-7, -6, -5, -4]
        self.assertEqual(max_integer(test_list), -4)

        test_list = [-4.22, -4.12, -4.10, -4.08]
        self.assertEqual(max_integer(test_list), -4.08)


    def test_none_and_zero(self):

        test_list = []
        self.assertEqual(max_integer(test_list), None)

        test_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(test_list), 0)
        self.assertEqual(max_integer(), None)

        test_list = {}
        self.assertEqual(max_integer(test_list), None)

        test_list = ()
        self.assertEqual(max_integer(test_list), None)


    def test_not_list(self):

        test_list = [1, "Cody", 3, 4]
        self.assertRaises(TypeError)

        test_list = [1, 2, [1, 2, 3], 4]
        self.assertRaises(TypeError)

        test_list = 9
        self.assertRaises(TypeError)

        test_list = 3.5
        self.assertRaises(TypeError)

        test_list = (4, 3, 2, 1)
        self.assertEqual(max_integer(test_list), 4)

        test_list = "Pixar"
        self.assertEqual(max_integer(test_list), 'x')

        test_list = 'Z'
        self.assertEqual(max_integer(test_list), 'Z')

if __name__ == '__main__':
    unittest.main()
