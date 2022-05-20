#!/usr/bin/python3
"""
Module containing rectangle
"""


class Rectangle:
    """
    class defining a rectangle with given height and width
    """
    def __init__(self, width=0, height=0):
        """
        initialize the object.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Gets the width for rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width for rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height for rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return for the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return for the parameter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
