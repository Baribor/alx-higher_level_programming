#!/usr/bin/python3
"""This module contains a `square class`
"""


class Square:
    """The Square class
    """

    def __init__(self, size=0):
        """Initializes the square instance

        Args:
            size (int, optional): Size of the Square. Defaults to 0.
        """
        self.size = size

    def area(self) -> int:
        """Computes the area of the Square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self) -> int:
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

    def __eq__(self, other) -> bool:
        """Performs == op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is equal to `other`
        """
        return self.size == other.size

    def __ne__(self, other) -> bool:
        """Performs != op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is not equal to `other`
        """
        return self.size != other.size

    def __gt__(self, other) -> bool:
        """Performs > op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is greater than to `other`
        """
        return self.size > other.size

    def __ge__(self, other) -> bool:
        """Performs >= op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is greater than or
            equal to `other`
        """
        return self.size >= other.size

    def __lt__(self, other) -> bool:
        """Performs < op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is less than `other`
        """
        return self.size < other.size

    def __le__(self, other) -> bool:
        """Performs <= op on Square

        Args:
            other (Square): The right operand

        Returns:
            bool: True if `self` is less than or equal to `other`
        """
        return self.size <= other.size


if __name__ == '__main__':
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
