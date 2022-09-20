#!/usr/bin/python3
"""
A module for division of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Division of matrix by div
    matrix: A list of list of numbers
    div: A number to divide the matrix
    Return: A new matrix of matrix / div
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = []
    for i in matrix:
        if (len(i) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for j in i:
            if (type(j) not in [int, float]):
                raise TypeError(err)
            temp.append(round(j/3, 2))
        newmatrix.append(temp)
    return newmatrix
    