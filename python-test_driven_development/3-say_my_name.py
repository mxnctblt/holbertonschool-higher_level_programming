#!/usr/bin/python3
# 3-say_my_name.py
""" function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ displays a name

    Args:
        first_name (str): First Name
        last_name (str): Last Name
    Raises:
        TypeError: if First_name or Last_name is not a str
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
