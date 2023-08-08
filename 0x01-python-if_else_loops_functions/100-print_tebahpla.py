#!/usr/bin/python3

is_lower = True

for i in range(26):
    l_ascii = 122 - i
    u_ascii = 90 - i
    print('{}'.format(chr(l_ascii if is_lower else u_ascii)), end="")
    is_lower = not is_lower
