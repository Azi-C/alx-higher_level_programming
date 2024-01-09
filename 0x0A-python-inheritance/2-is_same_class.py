#!/usr/bin/python3
"""class checks if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ returns True if object is exactly an instance of the specified class"""
    return type(obj) == a_class
