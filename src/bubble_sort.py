"""
Atharva's implementation of a bubble sort algorithm. Created for educative reference.
"""

"""
Given a list of integers, return the a list of integers sorted in non-decreasing order

Arguments:
    array (list): a list of integers

Returns:
    None: Sort array in place
"""

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array) - 1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]