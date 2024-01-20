#!/usr/bin/python3
"""writes a string to a text file and returns the number of characters written"""


def write_file(filename="", text=""):
    """using a a text file (UTF8)"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
