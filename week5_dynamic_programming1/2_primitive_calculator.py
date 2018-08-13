# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return 0 ,[1]


    min_ops = [0,0]
    origins = [0,1]
    for num in range(2, n + 1):
        m = float("inf") # minimum ops for current num
        origin = 0
        # add one
        adding = min_ops[num - 1] + 1
        if adding <= m:
            m = adding
            origin = num - 1
        # get there by mult by 2
        if num % 2 == 0:
            mult2 = min_ops[num//2] + 1
            if mult2 <= m:
                m = mult2
                origin = num // 2
        if num % 3 == 0:
            mult3 = min_ops[num//3] + 1
            if mult3 <= m:
                m = mult3
                origin = num // 3

        min_ops.append(m)
        origins.append(origin)



    # retrace your steps:
    path = []
    previous_pt = num
    while previous_pt != 1:
        current_pt = previous_pt
        path.append(current_pt)
        previous_pt = origins[current_pt]
    path.append(1)
    # reverse th path for correct order
    path.reverse()

    return min_ops[-1],path




input = sys.stdin.read()
#input = "3"
n = int(input)
min_ops, path = optimal_sequence(n)
print(min_ops)
for pt in path:
    print(pt, end = " ")