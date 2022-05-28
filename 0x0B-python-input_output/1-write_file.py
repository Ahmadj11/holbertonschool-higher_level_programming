#!/usr/bin/python3
""" write_file """




def write_file(filename="", text=""):
    """
    Write string to filename, it will be 
    created if filename doesn't exist, 
    and empty files will be overwritten """
    length = len(text)
    with open(filename, "w") as x:
        x.write(text)
    return length
