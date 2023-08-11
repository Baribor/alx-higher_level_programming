#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]

    if not len(args) == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if not args[1] in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    args_c = [int(i) if i.isdigit() else i for i in args]
    l, op, r = args_c
    ops_map = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    print("{} = {}".format(" ".join(args), ops_map[op](l, r)))
