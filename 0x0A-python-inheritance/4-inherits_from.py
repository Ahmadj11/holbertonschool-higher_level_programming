#!/usr/bin/python3
""" class that inherits from another class """


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    directly / indirectly from the specified class, otherwise return False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
