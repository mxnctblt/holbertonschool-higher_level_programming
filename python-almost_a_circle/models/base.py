#!/usr/bin/python3
""" module Base """
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ return a list of instances """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r") as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return (lst)
