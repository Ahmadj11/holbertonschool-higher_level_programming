#!/usr/bin/python3
"""
Module that contains the square subclass.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from superclass, Rectangle. Object of
    this class is defined by the attributes; size, x, and y.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Method to instantiates the object. Everyone of its attributes
        are instantiated using the init from the superclass.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the Square size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets for Square size.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Method to return a string representation of
        Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Method to assigns 'args' to each attribute. In order;
        id, width, height, x, and y. Or, if there is no 'args',
        then 'kwargs' will be used.
        """
        attrnum = 0
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[attrnum], arg)
                attrnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return a dictionary of the attributes of
        the Square.
        """
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}