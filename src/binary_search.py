"""
Atharva's implementation of a binary search algorithm. Created for educative reference.
"""

"""
Given a list of sorted integers, return the index of target integer using binary search. If target is not in list,
raise ValueError.

Arguments:
    array (list): a list of sorted integers 
    target (int): the integer being searched for

Returns:
    target_index (int): index position of target in list
"""


def binary_search(array, target):
    if len(array) == 0:
        raise ValueError("Cannot input a zero length array")
    elif len(array) == 1:
        if array[0] == target:
            return 0
        else:
            raise ValueError("Array does not contain target")
    else:
        mid = len(array) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search(array[mid:], target)
        elif array[mid] > target:
            return binary_search(array[:mid], target)