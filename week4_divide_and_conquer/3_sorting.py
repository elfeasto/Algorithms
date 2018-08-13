# Uses python3

"""
quick sort 3 with random pivot
"""
import sys
import random


def partition(A,l,r):
    """
    Rearranges the array around a pivot
    (which we arbitrarily take as A[l])
    such that the pivot is in its final position wrt the sorted
    array.
    i.e.
    everything to the left of the pivot is less than or equal to it
    everything to the right of the pivot is greater than it
    :param A: array
    :param l: lefmost index in question
    :param r: rightmost index in question
    :return: index j s.t. A[j] is in its final position
             (of the sorted array)
    """
    p_idx = random.randrange(l,r) # random pivot index
    #swap pivot to the first position in the array
    A[l] , A[p_idx] = A[p_idx], A[l]
    p = A[l] # assign pivot
    i = l + 1
    j = l
    k = l

    # pivot is at idx l, go from l+1 or r such that:
    # all pts in j are less than p
    # al pts from j+ 1 to k are equal to p
    # all pts from k+1 onwards are greater than p
    while i <= r:
        if A[i] > p:
            pass
        elif A[i] == p:
            # increment k and then
            # swap A[i] and a[k]
            k += 1
            A[k],  A[i] = A[i], A[k]
        else:
            j += 1
            k += 1
            # swap A[j] and A[i]
            # so up to j is sorted
            # but A[i] is now p
            A[j], A[i] = A[i], A[j]
            # swap A[k] and A[i]
            if k != j:
                A[k], A[i] = A[i], A[k]
        #print(j,k,i)

        i += 1
    #pivot is still at idx l so swap it into its correct place
    A[l], A[j] = A[j], A[l]
    return j,k


def quick_sort_inner(A,l,r):
    """
    MODIFIES the array passed in so that it is sorted
    DOES NOT RETURN A SORTED  ARRAY

    :param A: an array
    :param l: leftmost index we are considering
    :param r: rightmost index we are considering
    :return: None
    """
    if l >= r:
        return # One/no element(s) in A

    m,k = partition(A,l,r)
    # indices m to k will be in their final position
    quick_sort_inner(A,l, m - 1)
    quick_sort_inner(A,k+1,r)


def randomized_quick_sort(A):
    quick_sort_inner(A,0, len(A)-1)



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a)
    for x in a:
        print(x, end=' ')
