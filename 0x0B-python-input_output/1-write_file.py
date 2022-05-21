#!/usr/bin/python3
""" Using with to write a file"""

def write_file(filename=''):
    """ String for text and returns the number of characters """
    with open(filename) as f:
        return f.write(filename)
        print(len(f))