# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = []
        fib_list.append(0)
        fib_list.append(1)
        for _ in range(2,n + 1):
            fib_list.append((fib_list[-1] + fib_list[-2])%10)
        return fib_list[-1]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
