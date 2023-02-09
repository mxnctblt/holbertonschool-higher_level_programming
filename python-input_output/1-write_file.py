#!/usr/bin/python3
""" task 1 """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    xreturns the number of characters written """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
