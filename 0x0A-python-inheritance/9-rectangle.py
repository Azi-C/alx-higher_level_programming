#!/usr/bin/python3
"""class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
