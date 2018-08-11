import numpy as np
import random


def tests():
    test1 = [random.randint(1,100)]
    sorted_list = test1.sort()
    test1_array = np.array(test1)
    if np.array(sorted_list) == selection_sort(test1_array):
        return True


def selection_sort(array):
    """
    Sorts an array by moving the minimum element to the start
    on each loop through the array
    O(N**2)
    :param array:
    :return:
    """
    # we go through the array increasing the ordered part of it by 1
    # on each iteration(sorted from min to max, left to right)

    # left_idx is where we will place the smallest elt from the unsorted part of the list
    for left_idx in range(len(array)):
        min_idx = left_idx
        # find min elt of the yet to be sorted part of the array
        for j in range(left_idx, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        # swap the min elt with the elt at left_idx
        # so it is added to the sorted region on the LHS of the list
        array_idx = array[left_idx]
        array_min = array[min_idx]
        array[left_idx] = array_min
        array[min_idx] = array_idx

    return array



my_array = np.array([5,8,1,34,2])
print(my_array)
array_sorted = selection_sort(my_array)
print(array_sorted)




