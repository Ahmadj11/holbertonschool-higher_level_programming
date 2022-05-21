#!/usr/bin/python3
""" The student Class. """


class Student:
    """ Student Class. """

    def __init__(self, first_name, last_name, age):
        """ Initializing the Student. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary description of simple data structure 
        for JSON.
        """
        if type(attrs) is not list:
            return self.__dict__
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}