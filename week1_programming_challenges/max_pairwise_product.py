# Uses python3
num_inputs = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == num_inputs)

result = 0
max_elt = 0
max_elt_idx = 0
second_max_elt = 0

#find max elt
for idx in range(0, num_inputs):
    if a[idx] > max_elt:
        max_elt = a[idx]
        max_elt_idx = idx
#find second max elt
for idx in range(0, num_inputs):
    if idx == max_elt_idx:
        continue
    else:
        if a[idx] > second_max_elt:
            second_max_elt = a[idx]

result = max_elt * second_max_elt

print(result)
