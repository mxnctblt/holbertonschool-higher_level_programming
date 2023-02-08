#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """ define BaseGeometry """

    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
