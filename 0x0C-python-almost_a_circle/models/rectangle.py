#!/usr/bin/python3
"""
The `rectangle` module.
This module defines the Rectangle class
"""
from .base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor

        Args:
            width (int): width  of the rect
            height (int): height of the rect
            x (int, int): x coord. Defaults to 0.
            y (int, int): y cord. Defaults to 0.
            id (int, optional): rect id. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rect"""
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")

        self.__width = w

    @property
    def height(self):
        """height of the rect"""
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """x coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must >= 0")
        self.__x = x

    @property
    def y(self):
        """y coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must >= 0")
        self.__y = y

    def area(self):
        """computes the area of the rectangle

        Returns:
            int: the area
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(f"{' '*self.x}{'#' * self.width}")

    def __str__(self):
        """str rep of the rectangle"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """updates the rectangle
        """
        length = len(args)
        if (length > 0):
            if length > 0:
                self.id = args[0]
            if length > 1:
                self.width = args[1]
            if length > 2:
                self.height = args[2]
            if length > 3:
                self.x = args[3]
            if length > 4:
                self.y = args[4]
        else:
            if kwargs.get('id'):
                self.id = kwargs['id']

            if kwargs.get('x'):
                self.x = kwargs['x']

            if kwargs.get('y'):
                self.y = kwargs['y']

            if kwargs.get('width'):
                self.width = kwargs['width']

            if kwargs.get('height'):
                self.height = kwargs['height']

    def to_dictionary(self):
        """returns the dict rep of the rect

        Returns:
            dict: the dict rep of the rect
        """
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height
        }
