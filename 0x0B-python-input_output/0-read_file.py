#!/usr/bin/python3
""" Prints the text of a file to standard input """


def read_file(filename=""):
    """ prototype to read the file"""
    with open(filename) as f:
        print(f.read(), end='')
       
