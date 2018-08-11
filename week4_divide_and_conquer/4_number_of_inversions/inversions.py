# Uses python3
import numpy as np
import sys

def merge(a, b,a_invs, b_invs):
    """
    Merges two sorted Arrays
    AND
    Finds number of inversions
    :param a: Sorted array
    :param b: Sorted array
    :return: a and b merged and sorted and the number of invserions
    """
    # C will be our merged sorted array
    c = np.arange(len(a) + len(b))
    c_idx = 0
    a_idx = 0
    b_idx = 0
    num_inversions = 0

    while (a_idx != len(a) and b_idx != len(b)):
        if a[a_idx] <= b[b_idx]:
            c[c_idx] = a[a_idx]
            a_idx += 1
        else:
            c[c_idx] = b[b_idx]
            b_idx += 1
            num_inversions += len(a)  - a_idx
        c_idx += 1


    if a_idx != len(a):
        while a_idx != len(a):
            c[c_idx] = a[a_idx]
            a_idx += 1
            c_idx += 1
    if b_idx != len(b):
        while b_idx != len(b):
            c[c_idx] = b[b_idx]
            b_idx += 1
            c_idx += 1

    total_inversions = num_inversions + a_invs + b_invs
    return c, total_inversions


def merge_sort_inversions(a):
    # if A is size 1 return A and = inversions
    if len(a) == 1:
        return a, 0

    #find midpoint
    mid = int(len(a) / 2)
    # split A in two
    a_l = a[:mid]
    a_r = a[mid:]

    # recursively call merge_sort on both parts
    a_l, l_invs = merge_sort_inversions(a_l)
    a_r, r_invs = merge_sort_inversions(a_r)

    # merge the sorted arrays
    sorted_array, num_inversions = merge(a_l, a_r, l_invs, r_invs)
    return sorted_array, num_inversions


if __name__ == '__main__':
    input = "5 3 4 2 8 7"
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort_inversions(a)[1])
