#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """class that defines a square with Private instance attribute"""

    def __init__(self, size = 0):
        """
        Initializes the square

        Attributes:
            size: the size of a square
        Raises:
            TypeError: size must be an int
            ValueEroor: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
