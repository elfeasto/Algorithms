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

    p = A[l] # the pivot
    i = l + 1
    j = l
    while i <= r:
        if A[i] > p:
            pass
        else:
            j += 1
            # swap A[j] and A[i]
            A[j], A[i] = A[i], A[j]
        i += 1

    A[l], a[j] = A[j], A[l]
    return j


def quick_sort(A,l,r):
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

    m = partition(A,l,r)
    # a[m] will be in its final position
    quick_sort(A,l, m - 1)
    quick_sort(A,m+1,r)


a = [6,4,8,3,8,7,4,1]

quick_sort(a,0,7)
print(a)