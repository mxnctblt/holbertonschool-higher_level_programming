#!/usr/bin/python3
""" unittests for Base """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ testing Base """

    def test_id(self):
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

if __name__ == '__main__':
    unittest.main()
