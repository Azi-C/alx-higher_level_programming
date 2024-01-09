#!/usr/bin/python3
"""class that checks if object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance of a class"""
    return isinstance(obj, a_class)
