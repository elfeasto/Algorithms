# Uses python3
import sys
import numpy as np

def merge(A, majA, B, majB):
    """
    :param A:
    :param B:
    :return:
    """
    C = np.concatenate((A,B))
    majC = None
    if majA:
        count = 0
        for elt in C:
            if elt == majA:
                count += 1
        if count > int(len(C)/2):
            majC = majA
    if majB:
        count = 0
        for elt in C:
            if elt == majB:
                count += 1
        if count > int(len(C)/2):
            majC = majB

    return C, majC


def get_majority_element(a, maj_a):
    # case len = 1
    if len(a) == 1:
        return a, a[0]

    mid = int(len(a)/2)
    a_left = a[:mid]
    a_right = a[mid:]

    a_left, l_maj = get_majority_element(a_left, None)
    a_right, r_maj = get_majority_element(a_right, None)
    a, maj_a = merge(a_left, l_maj, a_right, r_maj)

    return a, maj_a


    #split array

if __name__ == '__main__':
    input = sys.stdin.read()
    len_a, *a = list(map(int, input.split()))
    a, ans = get_majority_element(a, None)
    if ans:
        print(1)
    else:
        print(0)

