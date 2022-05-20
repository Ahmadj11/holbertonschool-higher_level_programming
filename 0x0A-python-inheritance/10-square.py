#!/usr/bin/python3
"""
module that contains the square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
   class to creete the square object of size
    """
    def __init__(self, size):
        """
        method to create the object
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        method to return the area of an object.
        """
        return self.__size * self.__size
