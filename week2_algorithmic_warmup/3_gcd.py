# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def fast_gcd(a,b):
    if b == 0:
        return a
    else:
        reduced_a = a%b
        return fast_gcd(b, reduced_a)

if __name__ == "__main__":
    #input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(fast_gcd(a, b))
