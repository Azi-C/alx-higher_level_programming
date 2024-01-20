#!/usr/bin/python3
"""finction that reads a test file and prints it to stdout"""


def read_file(filename=""):
    """reads a file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
