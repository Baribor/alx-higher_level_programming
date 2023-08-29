#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        if not (isinstance(p, tuple) and all([isinstance(x, int) for x in p])):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = p

    def my_print(self):
        print(end='\n' * self.position[1])
        if self.size == 0:
            print(' ' * self.position[0])

        for i in range(self.size):
            print(f"{' ' * self.position[0]}{'#' * self.size}")


if __name__ == '__main__':
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
