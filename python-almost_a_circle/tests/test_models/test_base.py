#!/usr/bin/python3
""" unittests for Base """

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ testing Base """

    def test_a_id(self):
        """ testing id for task 1 """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(7)
        self.assertEqual(b5.id, 7)
        b6 = Base(11.5)
        self.assertEqual(b6.id, 11.5)
        b7 = Base('string')
        self.assertEqual(b7.id, 'string')
        b8 = Base([1, 2, 3, 4])
        self.assertEqual(b8.id, [1, 2, 3, 4])
        b9 = Base(-2)
        self.assertEqual(b9.id, -2)
        b10 = Base(0)
        self.assertEqual(b10.id, 0)
        b11 = Base({"a": 1, "b": 2})
        self.assertEqual(b11.id, {"a": 1, "b": 2})
        b12 = Base((1, 2, 3))
        self.assertEqual(b12.id, (1, 2, 3))
        b13 = Base(True)
        self.assertEqual(b13.id, True)
        b14 = Base(float('inf'))
        self.assertEqual(b14.id, float('inf'))
        b15 = Base(None)
        self.assertEqual(b15.id, 5)

    def test_to_json_string(self):
        """ testing to_json_string() for task 15 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string([]))
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)

    def test_save_to_file(self):
        """ testing save_to_file() for task 16 """
        r1 = Rectangle(10, 7, 2, 8, 11)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        s1 = Square(10, 7, 2, 8)
        s2 = Square(1, 2, 3, 4)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.isfile('Square.json'))

    def from_json_string(self):
        """ testing from_json_string() for task 17 """
        t1 = [{"id": 89, "width": 10, "height": 4}]
        f1 = Base.to_json_string(t1)
        self.assertEqual(list, type(f1))
        self.assertEqual(t1, f1)
        t2 = None
        f2 = Base.to_json_string(t2)
        self.assertEqual(f2, [])
        t3 = []
        f3 = Base.to_json_string(t3)
        self.assertEqual(t3, f3)
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)
        t4 = [
            {"id": 1, "width": 2, "height": 3, "x": 5, "y": 8},
            {"id": 6, "width": 7, "height": 4, "x": 9, "y": 10},
        ]
        f4 = Base.to_json_string(t4)
        self.assertEqual(t4, f4)

    def test_create(self):
        """ testing create() for task 18 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), '[Rectangle] (5) 3/4 - 1/2')
        self.assertEqual(r2.__str__(), '[Rectangle] (5) 3/4 - 1/2')
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), '[Square] (4) 2/3 - 1')
        self.assertEqual(s2.__str__(), '[Square] (4) 2/3 - 1')
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_load_from_file(self):
        """ testing load_from_file() for task 19 """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        r3 = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(r3[0]))
        self.assertEqual(str(r2), str(r3[1]))
        self.assertEqual(list, type(r3))
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        s3 = Square.load_from_file()
        self.assertEqual(str(s1), str(s3[0]))
        self.assertEqual(str(s2), str(s3[1]))
        self.assertEqual(list, type(s3))

if __name__ == '__main__':
    unittest.main()
