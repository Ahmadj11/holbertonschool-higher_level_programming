#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        contructs obkuct
        """
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(size, size)

    def area(self):
        """
        Area of object
        """
        return self.__size ** 2

    def __str__(self):
        """
        String method
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
