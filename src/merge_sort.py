"""
Atharva's implementation of a merge sort algorithm. Created for educative reference.
"""

"""
Given a list of integers, return a list of sorted integers

Arguments:
    array (list): a list of integers 

Returns:
    sorted (list): a list of integers, sorted in non-decreasing order
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    else: 
        middle = (len(array)) // 2
        left = merge_sort(array[:middle]) 
        right = merge_sort(array[middle:])
        i, j = 0, 0
        merge = []

        while i < len(left) and j < len(left):
            if left[i] <= right[j]:
                merge.append(left[i])
                i = i + 1
            elif left[i] > right[j]:
                merge.append(right[j])
                j = j + 1

        while i < len(left):
            merge.append(left[i])
            i = i + 1
        
        while j < len(right):
            merge.append(right[j])
            j = j + 1

        return merge