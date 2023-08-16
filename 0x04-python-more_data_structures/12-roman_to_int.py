#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    special_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                       'D': 500, 'M': 1000, '0': 0}
    num = 0
    prev = '0'

    for c in roman_string:
        if special_numbers[c] > special_numbers[prev]:
            num += special_numbers[c] - special_numbers[prev] * 2
        else:
            num += special_numbers[c]
        prev = c
    return num


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "MMMCMXCIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
