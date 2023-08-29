#!/usr/bin/python3

class Square:

    def __init__(self, size=0) -> None:
        self.size = size

    def area(self) -> int:
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def my_print(self):
        if self.size == 0:
            print()

        for i in range(self.size ** 2):
            print("#", end="")
            if i % self.size == self.size - 1:
                print()


if __name__ == '__main__':
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
