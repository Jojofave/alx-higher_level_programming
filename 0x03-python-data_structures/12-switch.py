#!/usr/bin/python3
def switch(a, b):
    """
    Switch the values of a and b

    :param a: first variable
    :param b: second variable
    :return: tuple containing a and b with their values switched
    """

    # Create a temporary variable to hold the value of a
    temp = a

    # Swap the values of a and b
    a = b
    b = temp

    return a, b
