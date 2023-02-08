#!/usr/bin/python3
""" module Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ define Rectangle """
    def __init__(self, width, height):
        """ initialize Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area Rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ string representation of Rectangle """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
