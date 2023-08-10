#!/usr/bin/python3
import sys

if __name__ == "__main__":
    _len = len(sys.argv)
    nums = [int(sys.argv[i]) for i in range(1, _len)]
    print("{}".format(sum(nums)))
