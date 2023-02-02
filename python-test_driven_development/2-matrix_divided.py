#!/usr/bin/python3
# 2-matrix_divided.py
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
         matrix : the matrix to divides
         div : the divisor
    Returns:
         returns new matrix of quotients
    Raises:
         TypeError: error if matrix is not a matrix
         ZeroDivisionError: error when div equal 0
         TypeError: error if div is not a number
    """
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            ' of integers/floats')
        if len(row) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        new_row = []
        for value in row:
            quot = round((value / div), 2)
            new_row.append(quot)
        new_matrix.append(new_row)
    return new_matrix
