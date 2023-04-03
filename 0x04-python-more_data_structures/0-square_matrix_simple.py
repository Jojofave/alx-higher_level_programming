#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    # Compute the square value of each integer in the input matrix and store it in the result matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
