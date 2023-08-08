#!/usr/bin/python3

def uppercase(str):
    s = len(str)
    empty = False

    if s == 0:
        s += 1
        empty = True

    for i in range(s):
        c = "." if empty else str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            end_char = "" if i < s - 1 else "\n"
            print("{}".format(chr(65 + (ord(c) - 97))), end=end_char)
            continue
        print("{}".format("" if empty else c), end="" if i < s - 1 else "\n")
        if empty:
            return
