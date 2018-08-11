# Uses python3
import sys
import numpy as np


def lottery(intervals, points):
    count = np.zeros(len(points), dtype=int)
    for interval in intervals:
        min_idx = leftmost(points, interval[0])
        max_idx = rightmost(points, interval[1])
        print(min_idx, max_idx)
        for idx in range(min_idx, max_idx):
            count[idx] += 1
    return count


def rightmost(array, key):
    #check if the elt is in the array and if so what index
    # otherwise index is where it would be inserted in the array
    is_elt, idx = inner_binary_search(array,key,0, len(array) - 1)
    if is_elt:
        return furthest_right(array,key, idx, len(array) - 1)
    else:
        # if idx == len(array):
        #     idx -= 1
        return idx


def leftmost(array,key):
    """

    :param array: sorted array
    :param key: item to find
    :return: tuple (bool, index)
    """
    is_elt, idx = inner_binary_search(array,key,0, len(array) - 1)
    if is_elt:
        return furthest_left(array,key, 0, idx)
    else:
        return idx


def inner_binary_search(array,key,low,high):
    if high < low:
        return (False, low)

    mid = low + int((high - low)/2)
    if array[mid] < key:
        return inner_binary_search(array, key, mid + 1, high)
    elif array[mid] > key:
        return inner_binary_search(array, key, low, mid - 1)
    else:
        return True, mid


def furthest_left(array, key, low, high):

    #check if ans is the leftmost elt of array
    if array[0] == key:
        return 0
    mid = low + int((high - low)/2)
    #check if on correct idx
    if array[mid] == key and array[mid - 1] != key:
        return mid
    elif array[mid] == key:
        return furthest_left(array, key, low, mid - 1)
    else:
        return furthest_left(array,key, mid + 1 , high)


def furthest_right(array, key, low, high):
    #check if ans is the leftmost elt of array
    if array[-1] == key:
        return len(array) - 1
    mid = low + int((high - low)/2)
    #check if on correct idx
    if array[mid] == key and array[mid + 1] != key:
        return mid
    elif array[mid] != key:
        return furthest_right(array, key, low, mid - 1)
    else:
        return furthest_right(array,key, mid + 1 , high)


if __name__ == '__main__':
    #input = sys.stdin.read()

    print(rightmost([0,10],11))


    input = "1 2 0 10 5 11"
    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    intervals = [[starts[idx], ends[idx]] for idx in range(len(starts))]
    points = data[2 * n + 2:]

    print("intervals are", intervals)

    sorted_indices = np.argsort(points) # indices of where the points will go when sorted
    points.sort()
    print("points are", points)
    cnt = lottery(intervals, points)
    print(cnt)



    # cnt_restored = [0 for p in points] # the count of each point mapped to their original position
    # for idx in range(len(cnt)):
    #     cnt_restored[sorted_indices[idx]] = cnt[idx]
    # for count in cnt_restored:
    #     print(count, end = " ")