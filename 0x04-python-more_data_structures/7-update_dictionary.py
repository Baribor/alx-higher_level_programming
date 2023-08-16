#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return dict(a_dictionary)


if __name__ == "__main__":
    psd = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    psd(new_dict)
    print("--")
    psd(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    psd(new_dict)
    print("--")
    psd(a_dictionary)
