#!/usr/bin/python3
""" creates a class named Square. """


class Square:
    """ square of a dictated size. """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        area = self.__size * self.__size
        return area