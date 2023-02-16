#!/usr/bin/python3
""" unittests for Rectangle """
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


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
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r4 = Rectangle(10, 2, 11.5, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5 = Rectangle(10, 2, 'string', 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(10, 2, [1, 2, 3, 4], 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r7 = Rectangle(10, 2, {1, 2, 3, 4}, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r8 = Rectangle(10, 2, float('inf'), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r9 = Rectangle(10, 2, float('nan'), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Rectangle(10, 2, True, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r11 = Rectangle(10, 2, b'hello', 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r12 = Rectangle(10, 2, bytearray(b'hello'), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r13 = Rectangle(10, 2, (1, 2, 3), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r14 = Rectangle(10, 2, {"a": 1, "b": 2}, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r15 = Rectangle(10, 2, frozenset({1, 2, 3}), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r16 = Rectangle(10, 2, range(2), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r17 = Rectangle(10, 2, complex(2), 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r18 = Rectangle(10, 2, memoryview(b'hello'), 0, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r19 = Rectangle(10, 2, -2, 0, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r20 = Rectangle(10, 2, -156, 0, 12)

    def test_y(self):
        """ testing y and its raises for tasks 2 & 3 """
        r1 = Rectangle(10, 2, 0, 7, 12)
        self.assertEqual(r1.y, 7)
        r2 = Rectangle(10, 2, 0, 7, 12)
        r2.y = 10
        self.assertEqual(r2.y, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Rectangle(10, 2, 0, None, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4 = Rectangle(10, 2, 0, 11.5, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5 = Rectangle(10, 2, 0, 'string', 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r6 = Rectangle(10, 2, 0, [1, 2, 3, 4], 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(10, 2, 0, {1, 2, 3, 4}, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r8 = Rectangle(10, 2, 0, float('inf'), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r9 = Rectangle(10, 2, 0, float('nan'), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Rectangle(10, 2, 0, True, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r11 = Rectangle(10, 2, 0, b'hello', 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r12 = Rectangle(10, 2, 0, bytearray(b'hello'), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r13 = Rectangle(10, 2, 0, (1, 2, 3), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r14 = Rectangle(10, 2, 0, {"a": 1, "b": 2}, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r15 = Rectangle(10, 2, 0, frozenset({1, 2, 3}), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r16 = Rectangle(10, 2, 0, range(2), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r17 = Rectangle(10, 2, 0, complex(2), 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r18 = Rectangle(10, 2, 0, memoryview(b'hello'), 12)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r19 = Rectangle(10, 2, 0, -2, 12)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r20 = Rectangle(10, 2, 0, -156, 12)

    def test_raises_order(self):
        """ testing raises order """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle('hey', 10, 'hey', 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2 = Rectangle(10, 'hey', 10, 'hey', 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(10, 10, 'hey', 'hey', 10)

    def test_area(self):
        """ testing area() for task 4 """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(10, 2, 0, 0, 12)
        r2.width = 7
        r2.height = 9
        self.assertEqual(r2.area(), 63)
        r3 = Rectangle(999, 999)
        self.assertEqual(r3.area(), 998001)
        r4 = Rectangle(10, 2, 0, 0, 12)
        with self.assertRaises(TypeError):
            r4.area(1)

    def test_display(self):
        """ testing display() for tasks 5 & 7 """
        r1 = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as test:
            r1.display()
            self.assertEqual(test.getvalue(),'##\n##\n##\n')
        r2 = Rectangle(2, 3, 2)
        with patch('sys.stdout', new=StringIO()) as test:
            r2.display()
            self.assertEqual(test.getvalue(), '  ##\n  ##\n  ##\n')
        r3 = Rectangle(2, 3, 0, 3)
        with patch('sys.stdout', new=StringIO()) as test:
            r3.display()
            self.assertEqual(test.getvalue(),'\n\n\n##\n##\n##\n')
        r4 = Rectangle(2, 3, 2, 3)
        with patch('sys.stdout', new=StringIO()) as test:
            r4.display()
            self.assertEqual(test.getvalue(),'\n\n\n  ##\n  ##\n  ##\n')

    def test_str(self):
        """ testing __str__() for task 6 """
        r1 = Rectangle(1, 2, 0, 0, 0)
        self.assertEqual(r1.__str__(), '[Rectangle] (0) 0/0 - 1/2')
        r2 = Rectangle(1, 2, 3, 0, 0)
        self.assertEqual(r2.__str__(), '[Rectangle] (0) 3/0 - 1/2')
        r3 = Rectangle(1, 2, 0, 4, 0)
        self.assertEqual(r3.__str__(), '[Rectangle] (0) 0/4 - 1/2')
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.__str__(), '[Rectangle] (5) 3/4 - 1/2')
        r5 = Rectangle(1, 2, 3, 4, 'test')
        self.assertEqual(r5.__str__(), '[Rectangle] (test) 3/4 - 1/2')

    def test_update_args(self):
        """ testing update() for task 8 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update()
        self.assertEqual(r1.__str__(), '[Rectangle] (5) 3/4 - 1/2')
        r2 = Rectangle(1, 2, 3, 4, 5)
        r2.update(6)
        self.assertEqual(r2.__str__(), '[Rectangle] (6) 3/4 - 1/2')
        r3 = Rectangle(1, 2, 3, 4, 5)
        r3.update(6, 7, 8)
        self.assertEqual(r3.__str__(), '[Rectangle] (6) 3/4 - 7/8')
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(6, 7, 8, 9, 10)
        self.assertEqual(r4.__str__(), '[Rectangle] (6) 9/10 - 7/8')
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.update(6, 7, 8, 9, 10, 11)
        self.assertEqual(r5.__str__(), '[Rectangle] (6) 9/10 - 7/8')
        r6 = Rectangle(1, 2, 3, 4, 5)
        r6.update(None)
        self.assertEqual(r6.__str__(), '[Rectangle] (None) 3/4 - 1/2')
        r6.update(-7)
        self.assertEqual(r6.__str__(), '[Rectangle] (-7) 3/4 - 1/2')
        r6.update('holberton')
        self.assertEqual(r6.__str__(), '[Rectangle] (holberton) 3/4 - 1/2')
        r7 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r7.update(7, 'string')
        r8 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r8.update(7, 0)
        r9 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r9.update(7, 8, 11.5)
        r10 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10.update(7, 8, 0)
        r11 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r11.update(7, 8, 9, b'hello')
        r12 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r12.update(7, 8, 9, -7)
        r13 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r13.update(7, 8, 9, 10, (1, 2, 3))
        r14 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r14.update(7, 8, 9, 10, -7)
        r15 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r15.update(7, 8, 'hey', 10, 'hey')

    def test_update_kwargs(self):
        """ testing update() for task 9 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(id=6)
        self.assertEqual(r1.__str__(), '[Rectangle] (6) 3/4 - 1/2')
        r2 = Rectangle(1, 2, 3, 4, 5)
        r2.update(width=7, id=6)
        self.assertEqual(r2.__str__(), '[Rectangle] (6) 3/4 - 7/2')
        r3 = Rectangle(1, 2, 3, 4, 5)
        r3.update(id=6, height=8, width=7)
        self.assertEqual(r3.__str__(), '[Rectangle] (6) 3/4 - 7/8')
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(width=7, id=6, x=9, height=8)
        self.assertEqual(r4.__str__(), '[Rectangle] (6) 9/4 - 7/8')
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.update(height=8, width=7, y=10, x=9, id=6)
        self.assertEqual(r5.__str__(), '[Rectangle] (6) 9/10 - 7/8')
        r6 = Rectangle(1, 2, 3, 4, 5)
        r6.update(height=8, y=10)
        self.assertEqual(r6.__str__(), '[Rectangle] (5) 3/10 - 1/8')
        r7 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r7.update(width='hey')
        r8 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r8.update(width=0)
        r9 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r9.update(height='hey')
        r10 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10.update(height=0)
        r11 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r11.update(x='hey')
        r12 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r12.update(x=-7)
        r13 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r13.update(y='hey')
        r14 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r14.update(y=-7)
        r15 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r15.update(height='hey', x='hey')

    def test_to_dictionary(self):
        """ testing to_dictionary() for task 13 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)
        r2 = Rectangle(1, 2, 3, 4, 'StarWars')
        d2 = {'id': 'StarWars', 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertDictEqual(r2.to_dictionary(), d2)
        r3 = Rectangle(7, 10, 0, 0, 5)
        d3 = {'id': 5, 'width': 7, 'height': 10, 'x': 0, 'y': 0}
        self.assertDictEqual(r3.to_dictionary(), d3)
        r4 = Rectangle(1, 2, 3, 4, 5)
        d4 = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertDictEqual(r4.to_dictionary(), d4)

if __name__ == '__main__':
    unittest.main()
