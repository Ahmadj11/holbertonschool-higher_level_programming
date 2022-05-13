#!/usr/bin/python3
def matrix_divided(matrix, div):
    if (div) is not int:
        raise TypeError ("div must be a number")
    elif (div) is 0:
        raise ZeroDivisionError ("division by zero")
    if (matrix) is not int:
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
