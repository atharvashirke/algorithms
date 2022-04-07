"""
Atharva's implementation of a counting sort algorithm. Created for educative reference.
"""

"""
Given a list of integers, return a list of sorted integers. 

Constraints: All values must between 0 and max_val.

Arguments:
    array (list): a list of integers
    max_val (int): largest val in list

Returns:
    None: Sorts list in place
"""

def counting_sort(array, max_val):
    counts = [0] * (max_val + 1)
    unsorted = array[:] 

    for num in array:
        counts[num] = counts[num] + 1
    
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i - 1]

    j = len(unsorted) - 1

    while j >= 0:
        index = counts[unsorted[j]] - 1
        array[index] = unsorted[j]
        counts[unsorted[j]] = counts[unsorted[j]] - 1
        j = j - 1
            



