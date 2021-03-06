#!/usr/bin/python3
"""
Module with the Base Geometry class
"""


class BaseGeometry:
    """
    Base geometry class
    """
    def area(self):
        """
        method to raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        make sure that the output is greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))                                                                                                                                                                                                        
~            
