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
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    elif first_name == "" and last_name == "":
        print()
    else:
        print(f"My name is {first_name} {last_name}")
