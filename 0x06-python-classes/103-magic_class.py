#!/usr/bin/python3
"""The MagicClass module
"""
import math


class MagicClass:
    """The MagicClass"""
    def __init__(self, radius) -> None:
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """The area method"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """The circumference method"""
        return 2 * math.pi * self.__radius
