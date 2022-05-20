#!/usr/bin/python3
""" The BaseGeometry class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits baseGeometry """
    def __init__(self, width, height):
        """ init method """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def __str__(self):
        """  method str """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ method for area """
        return self.__width * self.__height
