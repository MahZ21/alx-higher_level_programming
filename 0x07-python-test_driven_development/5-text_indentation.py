#!/usr/bin/python3
"""
A module to add two lines after ., :, and ? chars.
"""


def text_indentation(text):
    """
    prints a text with 2 lines after some chars
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    tmp = text.replace(".", ".\n\n")
    tmp = tmp.replace(":", ":\n\n")
    tmp = tmp.replace("?", "?\n\n")
    p = tmp.splitlines(True)
    ls_strip = []
    for i in p:
        if i == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(i.lstrip())
    print("".join(ls_strip), end="")
    