#!/usr/bin/python3
"""
The `square` module.
This module defines a Square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """The Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor

        Args:
            size (int): The size of the square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (_type_, optional): id of the square. Defaults to None.
        """
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    def __str__(self):
        """str rep

        Returns:
            str: The rep of the square instance
        """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Size of the square"""
        return self.height

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        """Updates the fields in the square
        """
        length = len(args)
        if (length > 0):
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]
        else:
            if kwargs.get('size'):
                self.size = kwargs['size']
            super().update(*args, **kwargs)

    def to_dictionary(self):
        """converts the square to a dictionary

        Returns:
            dict: dict rep of the square
        """
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.width,
        }
