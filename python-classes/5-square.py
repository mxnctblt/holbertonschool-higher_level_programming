#!/usr/bin/python3
# 5-square.py
"""Defines a class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initializes a square

        Args:
            size (int): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
