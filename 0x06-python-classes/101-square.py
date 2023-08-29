#!/usr/bin/python3
"""This module contains a `square class`
"""


class Square:
    """The Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """_summary_

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The x,y coordinate of the square.
            Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of the Square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """The `size` getter

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """The `size` setter

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size > 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """The position getter

        Returns:
            tuple: The x,y coordinate of the square
        """
        return self.__position

    @position.setter
    def position(self, p):
        """The position setter

        Args:
            p (tuple): The position of the square

        Raises:
            TypeError: If p is not a tuple or any item in p is not an int
        """
        if not (isinstance(p, tuple) and all([isinstance(x, int) for x in p])):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = p

    def my_print(self):
        """Prints the square
        """
        if self.size == 0:
            print()
            return

        print(end='\n' * self.position[1])

        for _ in range(self.size):
            print(f"{' ' * self.position[0]}{'#' * self.size}")

    def __str__(self) -> str:
        """The str rep of the Square

        Returns:
            str: The string rep of the Square
        """
        rep = []
        if self.size == 0:
            return ""
        rep.append('\n' * (self.position[1] - 1))
        for _ in range(self.size):
            rep.append(f"{' ' * self.position[0]}{'#' * self.size}")
        return '\n'.join(rep)


if __name__ == '__main__':
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
