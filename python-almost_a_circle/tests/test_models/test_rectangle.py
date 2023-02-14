#!/usr/bin/python3
""" unittests for Rectangle """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ testing Rectangle """

    def test_id(self):
        """ testing id for task 2 """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.id, 4)
        r5 = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(r5.id, 7)
        r6 = Rectangle(10, 2, 0, 0, 11.5)
        self.assertEqual(r6.id, 11.5)
        r7 = Rectangle(10, 2, 0, 0, 'string')
        self.assertEqual(r7.id, 'string')
        r8 = Rectangle(10, 2, 0, 0, [1, 2, 3, 4])
        self.assertEqual(r8.id, [1, 2, 3, 4])
        r9 = Rectangle(10, 2, 0, 0, -2)
        self.assertEqual(r9.id, -2)
        r10 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r10.id, 0)

    def test_width(self):
        """ testing width and its raises for tasks 2 & 3 """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(14, 2)
        self.assertEqual(r2.width, 14)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle(11.5, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r5 = Rectangle('string', 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r6 = Rectangle([1, 2, 3, 4], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r7 = Rectangle({1, 2, 3, 4}, 2)
        



if __name__ == '__main__':
    unittest.main()
