#!/usr/bin/python3
""" Task 1 - create a Base class """


class Base:
    """ defines Base

    Attributes:
        __nb_objects (int): the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the base

        Args:
            self: represents the instance of the class
            id (int): identity of the base
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
