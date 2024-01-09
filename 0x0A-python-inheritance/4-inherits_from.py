#!/usr/bin/python3
"""class that checks if object is an instance of a class that inherited from"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class"""
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
