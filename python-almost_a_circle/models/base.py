#!/usr/bin/python3
0;10;1c""" Task 1 - create a Base class """
import json


class Base:
    """ define Base

    Attributes:
        __nb_objects (int): the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base

        Args:
            self: represents the instance of the class
            id (int): identity of the base
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write the JSON string representation of list_objs to a file """
        with open('{:s}.json'.format(cls.__name__), "w") as fileo:
            if list_objs is None:
                fileo.write('[]')
            else:
                fileo.write(cls.to_json_string([cls.to_dictionary(x)
                                for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string representation json_string """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attributes already set """
        if cls.__name__ is "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ is "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ return a list of instances """
        res = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res
