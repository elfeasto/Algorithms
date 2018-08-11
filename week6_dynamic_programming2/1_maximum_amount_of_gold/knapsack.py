# Uses python3
import sys
import numpy as np

def max_value(weight, item_weights, item_values):
    """
    finds the maximum value of items that can be placed in a given knapsack of
    a given weight
    :param weight: max weight the knapsack can take(max capacity)
    :param item_weights: list of weights of each item
    :param item_values: list of values of each item
    :return: int: max value of items can fit in the knapsack
    """

    num_items = len(item_weights) # for convience
    # our answer array contains x + 1 since we have 0 to x inclusive on each axis
    max_values = np.zeros((num_items + 1, weight + 1), dtype = int)

    # add in zeros to start of these lists since so that index 1 matches item 1
    # rather than index 0 matches item 1
    item_weights = [0] + item_weights
    item_values = [0] + item_values

    # set sides as zero
    for n in range(num_items + 1):
        max_values[n][0] = 0
    for w in range(weight + 1):
        max_values[0][w] = 0

    #for each each max value either contains the nth item or it doesn't
    # so we look at each of these possibililities

    # for each cell the desired value is max of
    # max_values[n - 1][w] (without nth item)
    # OR
    # max_values[n - 1][w - item_weight] + item_values[n] (with nth item)
    for n in range(1, num_items + 1):
        for w in range(1, weight + 1):
            max_val = max_values[n - 1][w]
            item_weight = item_weights[n]
            if item_weight <= w: #checking (w - item_weight) is in the array
                other_val = max_values[n - 1][w - item_weight] + item_values[n]
                if other_val > max_val:
                    max_val = other_val
            max_values[n][w] = max_val

    return max_values[-1][-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    total_weight, num_items, *item_weights = list(map(int, input.split()))
    item_values = item_weights

    ans = max_value(total_weight, item_weights, item_values)
    print(ans)