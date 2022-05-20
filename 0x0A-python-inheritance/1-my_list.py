#!/usr/bin/python3
""" list class """


class MyList(list):
    """ class """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def print_sorted(self):
        """ Prints the list but in ascending order """
        print(sorted(self))
