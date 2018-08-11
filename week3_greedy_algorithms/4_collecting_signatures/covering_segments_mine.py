# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    print(segments)
    points = []
    # pick leftmost start interval
    # will have idx 0
    curr_segment = segments[0]
    # examine next segment on list
    next_segment = segments[1]
    # check if it is within the rightmost point of current segment
    # if not add point from anywhere in curr segment
    if curr_segment[1] < next_segment[0]:
        #break
        print('no overlap')
        points.append(curr_segment[0]) # any point on segment is fine
    else:
        # else go as far along the second segment while still
        # having a point in the first one
        print('is overlap')
        # check if current segment contains next segment
        if curr_segment[1] >= next_segment[1]:
            points.append(next_segment[1])
        else:
            points.append(curr_segment[1])
    return points

if __name__ == '__main__':
    #input = sys.stdin.read()
    input = "3 1 3 2 5 3 6"
    n, *data = (int(x)for x in input.split())
    segments = ( zip(data[::2], data[1::2]))
    segments = list(segments)

    points = optimal_points(segments)
    for p in points:
        print(p, end=' ')
