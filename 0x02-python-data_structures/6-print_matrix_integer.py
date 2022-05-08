#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        if x != 0:
            print()
        for b in range(len(matrix[x])):
            print("{:d}".format(matrix[x][b]), end="")
            if b != (len(matrix[x]) - 1):
                print(" ", end="")
    print("")
