#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for c in my_string:
        if not (c == 'c' or c == 'C'):
            new_str += c
    return new_str
