#!/usr/bin/python3
"""
Module that contains rectangle
"""


class Rectangle:
    """
    defines rectangle object on width and height.
    """
    def __init__(self, width=0, height=0):
        """
        initialize the rectangle
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
        Gets the rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        This string represents the rectangle using
        the '#' character.
        """
        rect_string = ""
        if self.width > 0 and self.height > 0:
            for x in range(self.__height):
                for y in range(self.__width):
                    rect_string += '#'
                if x != self.__height - 1:
                    rect_string += '\n'
        return rect_string
