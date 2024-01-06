#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """class that defines a rectangle with attributes"""

    def __init__(self, width=0, height=0):
        """
        Initialization

        Attributes:
            width, height (int): rectangle's informations

        Raises:
            TypeError: Attributes are not int
            ValueError: Attributes are less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter : returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Getter: get the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter: set the value of the height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
