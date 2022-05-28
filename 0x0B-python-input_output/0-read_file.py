#!/usr/bin/python3
"""
module that contains read_file
"""


def read_file(filename=""):
    """
    Reads filename and will print to standart output
    """
    with open(filename) as x:
        for line in x:
            print(line, end="")
