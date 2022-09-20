#!/usr/bin/python3
"""
A module for printing a square
"""


def print_square(size):
    """
    Prints square of size size
    """
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        print("#" * size)
        