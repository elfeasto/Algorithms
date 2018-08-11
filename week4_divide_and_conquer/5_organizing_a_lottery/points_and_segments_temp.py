# Uses python3
import sys
import numpy as np
import random
import time

def lottery(intervals, points):
    count = np.zeros(len(points), dtype=int)
    for interval in intervals:
        min_idx = leftmost(points, interval[0])
        max_idx = rightmost(points, interval[1])
        # print(min_idx, max_idx)
        for idx in range(min_idx, max_idx):
            count[idx] += 1
    return count


def rightmost(array, key):
    #check if the elt is in the array and if so what index
    #otherwise index is where it would be inserted in the array
    is_elt, idx = inner_binary_search(array,key,0, len(array) - 1)

    #if in the array go as far right as possible while
    # still on the key
    if is_elt:
        return furthest_right(array,key, idx, len(array) - 1)
    else:
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


def gen_data(num_segs, num_pts):

    segs = gen_segs(num_segs)
    pts = [random.randrange(-10**8, 10**8) for _ in range(num_pts)]
    ans_str = str(num_segs) + " "+ str(num_pts)
    segs_str = ""
    for idx in range(0,len(segs),2):
        segs_str += ( " " + str(segs[idx]) + " " + str(segs[idx + 1]) )
    pts_str = ""
    for pt in pts:
        pts_str += " " + str(pt)
    ans_str += segs_str
    ans_str += pts_str
    return ans_str


def gen_segs(num_segs):
    segs = []
    for _ in range(num_segs):
        left_pt = random.randrange(-10**8, 10**8)
        right_pt = random.randrange(left_pt, 10**8)
        segs.extend([left_pt,right_pt])
    return segs


if __name__ == '__main__':
    #input = sys.stdin.read()
    input = gen_data(10000, 10000)
    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]
    starts = data[2 : 2 * n + 2 : 2] #inteval start pts
    ends   = data[3 : 2 * n + 2 : 2] #interval end pts
    intervals = [[starts[idx], ends[idx]] for idx in range(len(starts))]
    points = data[2 * n + 2:]

    start = time.time()

    sorted_indices = np.argsort(points) # indices of where the points will go when sorted
    points.sort()

    cnt = lottery(intervals, points) # the count of each point in their sorted positions

    cnt_restored = [0 for p in points] # the count of each point mapped to their original position
    for idx in range(len(cnt)):
        cnt_restored[sorted_indices[idx]] = cnt[idx]
    # for count in cnt_restored:
    #     print(count, end = " ")
    print("done in", time.time()- start)
