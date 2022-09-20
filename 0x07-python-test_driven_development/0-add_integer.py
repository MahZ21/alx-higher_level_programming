#!/usr/bin/python3
"""
A module for addition of two numbers
"""


def add_integer(a, b=98):
    """
    Adds two numbers:
    a: Number 1
    b: Number 2, default 98.
    Return: int(a) + int(b)
    """
    try:
        assert type(a) in [int, float]
    except Exception:
        raise TypeError("a must be an integer")
    try:
        assert type(b) in [int, float]
    except Exception:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    