#!/usr/bin/python3

def uppercase(str):
    s = len(str)
    for i in range(s):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            print(chr(65 + (ord(c) - 97)), end="" if i < s - 1 else "\n")
            continue
        print(c, end="" if i < s - 1 else "\n")
