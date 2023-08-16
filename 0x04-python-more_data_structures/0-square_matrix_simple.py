#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    return [[n * n for n in i] for i in matrix]
