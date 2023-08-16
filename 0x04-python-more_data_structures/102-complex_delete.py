#!/usr/bin/python3

def complex_delete(a_dictionary: dict, value):
    if not a_dictionary or not isinstance(a_dictionary, dict):
        return

    keys = [k if v == value else None for k, v in a_dictionary.items()]
    for k in keys:
        if k:
            a_dictionary.pop(k)
    return dict(a_dictionary)


if __name__ == '__main__':
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
