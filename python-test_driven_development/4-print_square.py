#!/usr/bin/python3
# 4-print_square.py
""" function that prints a square with the character # """


def print_square(size):
    """ prints a square made of '#'

    Args:
        size (int): Size of square
    Raises:
        TypeError: if size is not an int
        ValueError: if size is negative or equal to zero
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is 0:
        print()
    else:
        for x in range(size):
            print("#" * size)
