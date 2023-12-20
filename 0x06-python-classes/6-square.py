#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """class that defines a square with Private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square

        Attributes:
            size (int): the size of a square
            position (int): the position of the square
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter : returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter : returns the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : set the position of the square"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """this method  prints in stdout the square  with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
