#!/usr/bin/python3
# 1-rectangle.py
"""Defines a class rectangle"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ initializes a rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve the width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieve the height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
