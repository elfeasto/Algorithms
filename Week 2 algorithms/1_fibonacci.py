# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = []
        fib_list.append(0)
        fib_list.append(1)
        for _ in range(2,n + 1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]

n = int(input())
print(calc_fib(n))
