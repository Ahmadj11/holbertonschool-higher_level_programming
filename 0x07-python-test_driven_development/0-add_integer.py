#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) is not int:
        raise TypeError ("a mustt be an integer")
    if type(b) is not int:
        raise TypeError ("b must be an integer")

