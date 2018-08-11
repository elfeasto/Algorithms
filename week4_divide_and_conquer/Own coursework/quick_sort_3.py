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
    k = l


    # all pts in j are less than p
    # al pts from j+ 1 to k are equal to p
    # all pts from k+1 onwards are greater than p
    while i <= r:
        print(i, A)
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
        print(j,k,i)

        i += 1
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


def quick_sort(A):
    quick_sort_inner(A,0, len(A)-1)




a = [8,6,4,8,6,6,7,2,1,6,7,10,12]
print("original array is", a)

partition(a,0,len(a)-1)
print(a)

quick_sort(a)
print(a)
