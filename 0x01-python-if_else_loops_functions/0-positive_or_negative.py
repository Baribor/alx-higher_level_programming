#!/usr/bin/python3
import random

number = random.randint(-10, 10)
if number == 0:
    print("{0:d} is zero".format(number))
else:
    remark = 'negative' if number < 0 else 'positive'
    print("{0:d} is {1:s}".format(number, remark))
