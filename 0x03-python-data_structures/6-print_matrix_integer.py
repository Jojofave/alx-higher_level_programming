#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to format the integer as a string and print it
            print("{:d}".format(row[i]), end="")
            # Print a space after each integer except for the last one in the row
            if i != len(row) - 1:
                print(" ", end="")
        # Print a newline after each row
        print()
