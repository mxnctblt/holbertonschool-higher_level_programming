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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__.copy()
