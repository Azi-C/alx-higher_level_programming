#!/usr/bin/python3
"""classe Base"""
import json
import csv


class Base:
    """manage id attribute in all the future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization function"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
