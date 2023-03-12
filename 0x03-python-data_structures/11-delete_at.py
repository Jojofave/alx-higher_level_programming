#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    :param my_list: list to be modified
    :param idx: index of the item to be deleted
    :return: the modified list
    """

    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list without the item at idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list
