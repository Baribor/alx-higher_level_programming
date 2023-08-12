#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        size = len(row)
        for i, num in enumerate(row):
            print("{:d}".format(num), end=" " if i + 1 < size else "")
        print()
