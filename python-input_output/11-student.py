#!/usr/bin/python3
""" students """


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        """ initializes the student's information
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.

        Otherwise, all attributes must be retrieved
        """
        if (type(attrs) == list and all(type(el) == str for el in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
