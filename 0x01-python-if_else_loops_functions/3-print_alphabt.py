#!/usr/bin/python3

for i in range(97, 123):
    if not chr(i) == 'e' and not chr(i) == 'q':
        print("{0:s}".format(chr(i)), end="")
