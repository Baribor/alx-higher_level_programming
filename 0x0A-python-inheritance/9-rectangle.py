#!/usr/bin/python3
"""The `5-base_geometry` module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class"""

    def __init__(self, width, height):
        """Initializes the object"""
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area"""
        return self.__width * self.__height

    def __str__(self):
        """The string rep"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
