#!/usr/bin/python3
"""The `10-square` module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Rectangle class"""

    def __init__(self, size):
        """Initializes the object"""
        self.integer_validator(size)
        self.__size = size

    def area(self):
        """computes the area"""
        return self.__size ** 2

    def __str__(self):
        """The string rep"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
