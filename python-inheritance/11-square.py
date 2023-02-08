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

    def area(self):
        """ returns area of square """
        return (self.__size ** 2)

    def __str__(self):
        """ string representation Square """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
