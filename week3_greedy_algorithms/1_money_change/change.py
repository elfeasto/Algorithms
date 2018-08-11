# Uses python3
import sys
import math

def get_change(m):
    #write your code here
    # first find number of tens then number of fives then singles

    currently_owed = m
    num_tens = math.floor(currently_owed / 10)

    currently_owed = m  - 10 * num_tens
    num_fives = math.floor(currently_owed / 5)

    currently_owed = currently_owed - 5 * num_fives
    num_ones = currently_owed

    ans = num_tens + num_fives + num_ones
    return ans

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
