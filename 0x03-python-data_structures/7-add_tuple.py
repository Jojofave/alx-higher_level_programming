#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Make sure tuple_a has at least 2 elements
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    # Make sure tuple_b has at least 2 elements
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    # Add the first elements of the tuples and the second elements of the tuples
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    # Return a tuple with the sums
    return (sum_a, sum_b)
