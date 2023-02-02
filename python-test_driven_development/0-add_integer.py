#!/usr/bin/python3
# 0-add_integer.py
""" function that adds 2 integers """


def add_integer(a, b=98):
    """ adds a and b

    Args:
        a (int): first number to add
        b (int) (by default 98): second number to add

    Returns:
        Reuturns a + b
    Raises:
        TypeError: error if a or b is not an integer
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
