#!/usr/bin/python3
"""The `5-base_geometry` module"""


class BaseGeometry:
    """The Base geometry class"""

    def area(self):
        """Computes the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a the value of a key"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
