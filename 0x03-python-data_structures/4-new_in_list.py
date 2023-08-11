#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    return [element if idx == i else my_list[i] for i in range(len(my_list))]
