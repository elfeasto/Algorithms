# Uses python3
from sys import stdin

def slow_get_fib_mod(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = []
        fib_list.append(0)
        fib_list.append(1)
        for _ in range(2,n + 1):
            next_fib_modded = (fib_list[-1] + fib_list[-2]) % mod
            fib_list.append(next_fib_modded)
        return fib_list[-1]

def get_fib_period(mod):
    assert mod > 1
    # want a list of fib numbers mod n until we find the period
    # period is found when we repeat 0,1
    period_found = False
    first_match = False
    fib_idx = 2
    while not period_found:
        if first_match:
            if slow_get_fib_mod(fib_idx, mod) == 1:
                period_found = True
            else:
                first_match = False
        else:
            if slow_get_fib_mod(fib_idx, mod) == 0:
                first_match = True

        fib_idx += 1
    return fib_idx - 2


def fast_get_fib_mod(n, mod):
    period = get_fib_period(mod)
    equivalent_fib_idx = n % period
    equivalent_fib_mod = slow_get_fib_mod(equivalent_fib_idx, mod)
    return equivalent_fib_mod

def fib_sum_squares_mod10(n):
    fib_n = fast_get_fib_mod(n, 10)
    return ( fib_n * (fib_n + fast_get_fib_mod(n-1,10) ) ) % 10

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_squares_mod10(n))
