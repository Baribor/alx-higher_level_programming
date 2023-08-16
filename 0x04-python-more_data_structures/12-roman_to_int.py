#!/usr/bin/python3

def roman_to_int(roman_string):
    special_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    
    for c in roman_string[::-1]:
        if special_numbers[c] < num:
            num -= special_numbers[c]
            continue
        num += special_numbers[c]
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
		