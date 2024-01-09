#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method  that validates value"""
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
