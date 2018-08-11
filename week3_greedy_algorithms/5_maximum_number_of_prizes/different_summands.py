# Uses python3
import sys

def naturals_sum(n):
    if n % 2 == 0:
        temp = int(n/2)
        return temp *(n+1)
    else:
        temp = int((n+1)/2)
        return temp * n

def optimal_summands(n):
    #use sum of first n natural numbers
    counter = 1
    while naturals_sum(counter + 1) <= n:
        counter += 1

    ans = list(range(1,counter + 1))
    # add in the left over to the last entry
    ans[-1] += n - naturals_sum(counter)

    return ans

if __name__ == '__main__':
    #input = sys.stdin.read()
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
