#!/usr/bin/python3
""" module Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ define Square """
    def __init__(self, size):
        """ initialiaze Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
