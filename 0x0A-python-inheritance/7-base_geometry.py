#!/usr/bin/python3
""" The BaseGeometry class """


class BaseGeometry:
    """A BaseGeometry class """
    def area(self):
        """ method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate the int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
            return False
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            return False
        else:
            return value
