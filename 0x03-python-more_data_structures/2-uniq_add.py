#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    sum of all unique elements within the list.
    """
    new_list = [element for element in my_list]
    return sum(set(new_list))
