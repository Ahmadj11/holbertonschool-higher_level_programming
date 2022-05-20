#!/usr/bin/python3
"""
Module containing the rectangle
"""


class Rectangle:
    """
    defines a Rectangle object with given width & height.
    """
    def __init__(self, width=0, height=0):
        """
        initializes the object.
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
        Getter for the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height for rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
