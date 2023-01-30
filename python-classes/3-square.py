#!/usr/bin/python3
# 3-square.py
"""Defines a class Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initializes a square

        Args:
            size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
