# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    unit_values = ((values[n]/weights[n],n) for n in range(len(values)))
    sorted_values = sorted(unit_values, key = lambda values:values[0])

    value_carried = 0

    while capacity != 0:
        #check if stuff left to put in to bag
        if not sorted_values:
            break
        most_val_idx = sorted_values.pop()[1]
        # add as much as possible of most valuable to bag
        if capacity >= weights[most_val_idx]:
            percent_to_add = 1
        else:
            percent_to_add = capacity / weights[most_val_idx]

        value_carried += percent_to_add * values[most_val_idx]
        capacity -= percent_to_add * weights[most_val_idx]

    return value_carried


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
