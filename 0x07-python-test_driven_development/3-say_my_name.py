#!/usr/bin/python3
"""
This is a module for printing first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is firstname lastname
    first_name: First Name input
    last_name: Last name input
    """
    err = "first_name must be a string"
    err1 = "last_name must be a string"
    if (type(first_name) is not str):
        raise TypeError(err)
    if (type(last_name) is not str):
        raise TypeError(err1)
    print("My name is {} {}".format(first_name, last_name))
    