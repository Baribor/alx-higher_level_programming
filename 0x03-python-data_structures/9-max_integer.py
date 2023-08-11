#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    _max = my_list[0]

    for num in my_list:
        if num > _max:
            _max = num
    return _max
