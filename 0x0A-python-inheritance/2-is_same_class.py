#!/usr/bin/python3
"""The `2-is_same_class` module"""


def is_same_class(obj, a_class) -> bool:
    """Checks if an object is an instance of a class

    Args:
        obj (any): Object to check
        a_class (any): Class

    Returns:
        bool: True if the object is exactly an
        instance of the specified class ; otherwise False.
    """
    return issubclass(a_class, obj)


if __name__ == '__main__':
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
