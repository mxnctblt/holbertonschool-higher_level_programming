#!/usr/bin/python3
""" module Rectangle """
from models.base import Base


class Rectangle(Base):
    """ define Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coorfinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
