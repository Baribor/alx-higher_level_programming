#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_a = [0] * 2
    new_b = [0] * 2
    for i, n in enumerate(tuple_a):
        if i > 1:
            break
        new_a[i] = n
    for i, n in enumerate(tuple_b):
        if i > 1:
            break
        new_b[i] = n
    return (new_a[0]+new_b[0], new_a[1]+new_b[1])
