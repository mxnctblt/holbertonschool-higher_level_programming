#!/usr/bin/python3
""" module Rectangle """
from models.base import Base


class Rectangle(Base):
    """ define Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coorfinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ retrieve the width of the rectangle """
            return (self.__width)

        @width.setter
        def width(self, value):
            """ set the width of the rectangle """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be >= 0")
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
            elif value <= 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        @property
        def x(self):
            """ retrieve the x coordinate of the rectangle """
            return self.__x

        @x.setter
        def x(self, value):
            """ set the x coordinate of the rectangle """
            self.__x = value

        @property
        def x(self):
            """ retrieve the x coordinate of the rectangle """
            return self.__x

        @y.setter
        def y(self, value):
            """ set the y coordinate of the rectangle """
            self.__y = value
