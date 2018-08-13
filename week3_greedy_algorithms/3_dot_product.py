#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort()
    b.sort()
    running_total = 0

    while a:
        if a[0] * b[0] >= a[-1] * b[-1]:
            running_total += a[0] * b[0]
            del a[0]
            del b[0]
        else:
            running_total += a[-1] * b[-1]
            del a[-1]
            del b[-1]
    return running_total


def naive_max_dot(a,b):
    running_total = 0
    biggest_a_idx = 0
    biggest_b_idx = 0
    while a:
        biggest = float("-inf")
        for idx_a in range(len(a)):
            for idx_b in range(len(b)):
                product = a[idx_a] * b[idx_b]
                if product > biggest:
                    biggest = product
                    biggest_a_idx = idx_a
                    biggest_b_idx = idx_b
        running_total += a[biggest_a_idx] * b[biggest_b_idx]
        del a[biggest_a_idx]
        del b[biggest_b_idx]

    return running_total




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
