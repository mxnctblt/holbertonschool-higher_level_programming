#!/usr/bin/python3
"""
A module that test differents behaviors
of the Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """

    def test_getter(self):
        r1 = Square(5)
        self.assertEqual(r1.size, 5)

    def test_setter(self):
        r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)

    def test_string(self):
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = "Hi"

    def test_negative(self):
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = -5
    def test_zero(self):
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = 0

    def test_decimal(self):
        r1 = Square(6)
        with self.assertRaises(TypeError):
            r1.size = 1.5

    def test_tuple(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = (2, 8)

    def test_empty(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = ''

    def test_none(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = None

    def test_list(self):
        r1 = Square(4)
        with self.assertRaises(TypeError):
            r1.size = [4, 7]

    def test_dict(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = {"hi": 5, "world": 8}

    def test_width(self):
        r1 = Square(5)
        r1.size = 6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected)

        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)

        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)

    def test_missing(self):
        s1 = Square(1, 2)
        self.assertEqual(s1.x, 2)
        s2 = Square(1, 2, 3)
        self.assertEqual(s2.y, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s4 = Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s5 = Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s6 = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s7 = Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s8 = Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s9 = Square(1, 2, -3)
