#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the result
    result_list = []

    # Iterate over each element in the input list
    for element in my_list:
        # If the current element is the one we want to replace, add the replacement element to the result list
        if element == search:
            result_list.append(replace)
        # Otherwise, add the current element to the result list
        else:
            result_list.append(element)

    return result_list
