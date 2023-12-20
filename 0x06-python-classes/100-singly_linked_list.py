#!/usr/bin/python3
"""class that defines a node"""


class Node:
    """class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Initializes node

        Attributes:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data

