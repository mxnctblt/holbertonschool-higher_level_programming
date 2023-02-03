#!/usr/bin/python3
# 6-rectangle.py
"""Defines a class rectangle"""


class Rectangle:
    """defines a rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initializes a rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the rectangle's area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """ returns a rectangle in char '#' """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            if i == self.__height - 1:
                rec += ('#' * self.__width)
            else:
                rec += (('#' * self.__width) + '\n')
        return rec

    def __repr__(self):
        """ return the string representation of the rectangle """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ prints a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
