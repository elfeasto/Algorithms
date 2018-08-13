# Uses python3
import sys

def my_binary_search(a, key, l, r):
    if l > r :
        return - 1
    mid = l +  int((r - l)/2)
    if a[mid] == key:
        return mid
    elif a[mid] < key:
        return my_binary_search(a, key, mid + 1 , r)
    else:
        return my_binary_search(a,key, l, mid - 1)

def binary_search(a, key):
    left, right = 0, len(a) - 1
    # write your code here
    return my_binary_search(a,key,left,right)

def linear_search(a, x):
    print(a)
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
