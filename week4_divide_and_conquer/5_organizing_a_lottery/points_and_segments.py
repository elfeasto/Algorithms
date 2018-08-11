# Uses python3
import sys
import numpy as np
#import Lottery_test_data as data


def lottery(intervals, points):
    """
    intervals and points should be sorted ascendingly
    :param intervals:
    :param points:
    :return:
    """
    counts = np.zeros(len(points), dtype = int) # number of times each point is in one of the intervals
    i_idx = 0 #intervals index
    p_idx = 0 # pts index


    while (p_idx < len(points) and i_idx < len(intervals)):
        # pt to left of current and therefore all intevals
        if points[p_idx] < intervals[i_idx][0]:
            p_idx += 1
        #pt to right of current interval
        elif points[p_idx] > intervals[i_idx][1]:
            i_idx += 1
        #pt inside current inteval
        else:
            j_idx = i_idx # j_idx is temporary index for the intervals
            while (j_idx < len(intervals) and intervals[j_idx][0] <= points[p_idx]):
                if points[p_idx] <= intervals[j_idx][1]:
                    counts[p_idx] += 1
                j_idx += 1
            p_idx += 1

    return counts


def sort_intervals(intervals):
    """
    reorders so that the lower elt is first in each pair
    then orders then tuples by the first point
    :param intervals: list of pairs
    :return: ordered and sorted list of pairs
    """
    for pair in intervals:
        if pair[0] > pair[1]:
            pair[0] , pair[1] = pair[1], pair[0]

    ans = sorted(intervals, key=lambda x: x[0])

    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    intervals = [[starts[idx], ends[idx]] for idx in range(len(starts))]

    intervals = sort_intervals(intervals)
    sorted_indices = indices = np.argsort(points) # indices of where the points will go when sorted
    points.sort()

    cnt = lottery(intervals, points)
    cnt_restored = [0 for p in points] # the count of each point mapped to their original position
    for idx in range(len(cnt)):
        cnt_restored[sorted_indices[idx]] = cnt[idx]

    for x in cnt_restored:
        print(x, end=' ')
