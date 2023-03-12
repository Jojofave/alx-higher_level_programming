def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one integer per line.

    Args:
        my_list (list of int): The list of integers to print. Default is an empty list.

    Returns:
        None
    """
    for integer in my_list:
        print("{:d}".format(integer))
