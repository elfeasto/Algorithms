import numpy as np
import random


def merge(A,B):
    """
    Merges two sorted Arrays
    :param A:
    :param B:
    :return:
    """
    # C will be our merged sorted array
    C = np.arange(len(A) + len(B))
    C_idx = 0
    A_idx = 0
    B_idx = 0

    while (A_idx != len(A) and B_idx != len(B)):
        if A[A_idx] < B[B_idx]:
            C[C_idx] = A[A_idx]
            A_idx += 1
        else:
            C[C_idx] = B[B_idx]
            B_idx += 1
        C_idx += 1


    if A_idx != len(A):
        while A_idx != len(A):
            C[C_idx] = A[A_idx]
            A_idx += 1
            C_idx += 1
    if B_idx != len(B):
        while B_idx != len(B):
            C[C_idx] = B[B_idx]
            B_idx += 1
            C_idx += 1

    return C


def merge_sort(A):
    # if A is size 1 return A
    if len(A) == 1:
        return A

    #find midpoint
    mid = int(len(A)/2)
    # split A in two
    A_l = A[:mid]
    A_r = A[mid:]

    # recursively call merge_sort on both parts
    A_l = merge_sort(A_l)
    A_r = merge_sort(A_r)

    # merge the sorted arrays
    ans = merge(A_l, A_r)
    return ans


A = np.array([random.randint(1,100) for _ in range(100)])
A_sorted = merge_sort(A)
print(A_sorted)
