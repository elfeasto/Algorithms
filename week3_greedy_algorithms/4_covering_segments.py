# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def reaches_next(segments, idx, furthest_right):
    if furthest_right >= segments[idx + 1][0]:
        return True
    else:
        return False

def segments_remain(curr_idx, end_idx):
    if curr_idx + 1 <= end_idx:
        return True
    else:
        return False


def optimal_points(segments):
    #print(segments)
    # sort the segements by first point
    segments = sorted(segments, key = lambda x: x[0])
    end_idx = len(segments) - 1
    points = []
    covered_idx = -1
    while covered_idx != end_idx:
        covered_idx += 1
        furthest_right = segments[covered_idx][1]
        #print('index to test', covered_idx, end='   |   ')

        while segments_remain(covered_idx, end_idx) and (reaches_next(segments, covered_idx, furthest_right)):
            covered_idx += 1
            furthest_right = min(furthest_right, segments[covered_idx][1])
        #print('index we get to', covered_idx)
        points.append(furthest_right)



    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = (int(x)for x in input.split())
    segments = ( zip(data[::2], data[1::2]))
    segments = list(segments)

    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p)