#!/usr/bin/python3
""" module Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize Square

        Args:
            size (int): size of the square
            x (int): x coorfinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size> """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """ retrieve the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns a key/value argument to attributes """
        if kwargs and kwargs != "":
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif args and args != "":
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """ return the dictionary representation of a Square """
        a = ['id', 'x', 'size', 'y']
        b = [self.id, self.x, self.width, self.y]
        dict = {}
        for i in range(len(a)):
            dict[a[i]] = b[i]
        return dict
