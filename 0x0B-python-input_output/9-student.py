#!/usr/bin/python3
""" Student Class defing by first and last name,
 and age.  
 """


class Student:
    """ The Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initializing the Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve a dictionary representation of a Student """
        return self.__dict__