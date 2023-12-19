#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """class that defines a square with Private instance attribute"""

    def __init__(self, size=0):
        """
        Initializes the square

        Attributes:
            size (int): the size of a square
        Raises:
            TypeError: size must be an int
            ValueEroor: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

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

    def area(self):
        """This function returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """this method  prints in stdout the square  with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("\n")
