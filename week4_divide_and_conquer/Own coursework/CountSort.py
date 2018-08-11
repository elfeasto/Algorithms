import numpy as np


def count_sort(A,m):
    """
    Sorts an array consisting ONLY of the first m integers
    :param A: np array
    :param m: integer, max integer in A
    :return: A sorted
    """

    print("Input is", A)
    # create our count array, size m + 1 to include 0
    count = np.zeros(m + 1, dtype = int)
    for idx in range(len(A)):
        count[A[idx]] += 1
    print("count array is:", count)

    pos = np.zeros(m + 1, dtype = int)
    pos[0] = 0
    for idx in range(1,len(count)):
        pos[idx] = pos[idx-1] + count[idx-1]
    print("postition array is:", pos)

    A_s = np.zeros(len(A), dtype = int) # A sorted
    for idx in range(len(A)):
        a = A[idx]
        A_s[pos[a]] = a
        pos[a] += 1


    print("sorted array is:", A_s)


    return A_s



A = np.array([0,3,3,2,5,5,2,3,0,2,1,2])
sorted = count_sort(A, 5)
print(sorted)
