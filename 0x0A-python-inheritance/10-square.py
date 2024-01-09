#!/usr/bin/python3
""" class Square"""


Rectangle = __import('9-rectangle')Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        super.__init__(size, size)
        self.__size = size
