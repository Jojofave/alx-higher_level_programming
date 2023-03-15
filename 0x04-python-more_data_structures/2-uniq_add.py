#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over each element in the input list
    for element in my_list:
        # If the current element is an integer, add it to the set of unique integers
        if isinstance(element, int):
            unique_integers.add(element)

    # Return the sum of all unique integers
    return sum(unique_integers)
