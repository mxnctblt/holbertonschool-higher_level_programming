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
