#!/usr/bin/python3
"""
Module that contains Rectangle subclass
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits from superclass, Base. A object of this
    class will be defined by its private attributes; width, height, x,
    and y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method to instantiate the object. The id is
        instantiated with the init from the superclass.
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """
        Getter for the Rectangle width.
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for the Rectangle height.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter for the Rectangle x.
        """
        return self.__x

    @property
    def y(self):
        """
        Getter for the Rectangle y.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter for the Rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the Rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the Rectangle x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the Rectangle y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method to return the area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle to standard output using the character '#'.
        """
        for lines in range(self.__y):
            print()
        for row in range(self.__height):
            for spot in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Method to returns string representation of the
        Rectangle.
        """
        return "[Rectangle] \
({}) {}/{} - {}/{}".format(self.id, self.__x,
                           self.__y, self.__width,
                           self.__height)

    def update(self, *args, **kwargs):
        """
        Method assigns 'args' to each attribute. In order;
        id, width, height, x, and y. Or, if there is no 'args',
        then 'kwargs' will be used.
        """
        attrnum = 0
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[attrnum], arg)
                attrnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return the dictionary representation of
        the Rectangle.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}