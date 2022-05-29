#!/usr/bin/python3
"""
Module containing the class: Base.
"""
import json
import os


class Base:
    """
    This is the base class that everything will inherit from.
    nb_objects a private attribute that gives an id
    to any object that was created without one.
    """
    __nb_objects = 0

    @classmethod
    def clear(cls):
        """
        Method to reset the nb_ojects.
        """
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """
        Method for intantiation.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method to return the JSON format of 'list_dictionaries'.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method to write JSON string representation of 'list_objs' to a file.
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Method to return list of the JSON string, 'json_string'.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method to return a object with the attributes set by
        kwargs, 'dictionary'.
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        Method return the list of how many instances of a particular
        class, 'cls'.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            newlist = cls.from_json_string(file.read())
        newobj = []
        for dict in newlist:
            newobj.append(cls.create(**dict))
        return newobj