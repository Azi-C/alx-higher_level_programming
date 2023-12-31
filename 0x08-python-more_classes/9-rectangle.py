#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    """class that defines a rectangle with attribute"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialiszes the Rectangle

        Attributes:
            width, height (int): of the rectangle

        Raises:
            TypeError: Attributes are not an int
            ValueError: Attributes are less than 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter : returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter : set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter : returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter : set the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance : that returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance : that returns the rectangle perimeter"""
        if self.__width and self.__height != 0:
            return (self.__width * 2) + (self.__height * 2)
        return 0

    def __str__(self):
        """printf a rectangle using #"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        s = "\n".join([str(self.print_symbol) * self.__width
                       for rows in range(self.__height)])
        return s

    def __repr__(self):
        """string representation to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints a message after deleting a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
        return rect_2
