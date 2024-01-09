#!/usr/bin/python3
"""
parent class BaseGeometry
subclass Rectangle
subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
