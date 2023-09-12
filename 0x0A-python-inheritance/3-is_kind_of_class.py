#!/usr/bin/python3
"""The `3-is_kind_of_class` module"""


def is_kind_of_class(obj, a_class) -> bool:
    """Checks if an object is an instance of a class

    Args:
        obj (any): Object to check
        a_class (any): Class

    Returns:
        bool: True if the object is exactly an
        instance of the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)

