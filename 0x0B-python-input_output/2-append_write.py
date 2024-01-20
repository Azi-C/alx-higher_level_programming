#!/usr/bin/python3
"""appends a string at the end and returns the number of char added"""


def append_write(filename="", text=""):
    """a text file (UTF8)"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
