#!/usr/bin/python3
""" unittests for Rectangle """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ testing Rectangle """

    def test_id(self):
        """ testing id for task 2 """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        r3 = Rectangle(10, 2)
        r4 = Rectangle(10, 2)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r3.id - 1)
        self.assertEqual(r3.id, r4.id - 1)
        self.assertEqual(r4.id, r2.id + 2)
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
        r2 = Rectangle(10, 2)
        r2.width = 14
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
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r8 = Rectangle(float('inf'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r9 = Rectangle(float('nan'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r11 = Rectangle(b'hello', 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r12 = Rectangle(bytearray(b'hello'), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r13 = Rectangle((1, 2, 3), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r14 = Rectangle({"a": 1, "b": 2}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r15 = Rectangle(frozenset({1, 2, 3}), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r16 = Rectangle(range(2), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r17 = Rectangle(complex(2), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r18 = Rectangle(memoryview(b'hello'), 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r19 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r20 = Rectangle(-2, 2)

    def test_height(self):
        """ testing height and its raises for tasks 2 & 3 """
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.height, 10)
        r2 = Rectangle(2, 10)
        r2.height = 14
        self.assertEqual(r2.height, 14)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r3 = Rectangle(2, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r4 = Rectangle(2, 11.5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(2, 'string')
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r6 = Rectangle(2, [1, 2, 3, 4])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r7 = Rectangle(2, {1, 2, 3, 4})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r8 = Rectangle(2, float('inf'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r9 = Rectangle(2, float('nan'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r10 = Rectangle(2, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r11 = Rectangle(2, b'hello')
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r12 = Rectangle(2, bytearray(b'hello'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r13 = Rectangle(2, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r14 = Rectangle(2, {"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r15 = Rectangle(2, frozenset({1, 2, 3}))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r16 = Rectangle(2, range(2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r17 = Rectangle(2, complex(2))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r18 = Rectangle(2, memoryview(b'hello'))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r19 = Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r20 = Rectangle(2, -2)

    def test_x(self):
        """ testing x and its raises for tasks 2 & 3 """
        r1 = Rectangle(10, 2, 7, 0, 12)
        self.assertEqual(r1.x, 7)
        r2 = Rectangle(10, 2, 7, 0, 12)
        r2.x = 10
        self.assertEqual(r2.x, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(10, 2, None, 0, 12)
    def test_y(self):
        """ testing y and its raises for tasks 2 & 3 """
        r1 = Rectangle(10, 2, 0, 7, 12)
        self.assertEqual(r1.y, 7)
        r2 = Rectangle(10, 2, 0, 7, 12)
        r2.y = 10
        self.assertEqual(r2.y, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Rectangle(10, 2, 0, None, 12)

if __name__ == '__main__':
    unittest.main()
