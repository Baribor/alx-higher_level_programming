#!/usr/bin/python3
import sys

if __name__ == "__main__":
    _len = len(sys.argv) - 1
    print("{} argument{}".format(_len, "" if _len == 1 else "s"), end="")
    if _len == 0:
        print(".")
        sys.exit()
    print(":")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{}: {}".format(i, arg))
