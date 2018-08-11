# Uses python3
import sys
import numpy as np


def DPChange(target_money,coins):

    min_num_coins = np.zeros(target_money + 1, dtype = int)
    min_num_coins[0] = 0

    # for each amount of money before target money
    # find the min num coins possible
    for money in range(1,target_money +1):
        # find min num coins for money
        min_coins = float("inf")
        for coin in coins:
            if coin <= money:
                num_coins = 1 + min_num_coins[money - coin]
                if num_coins <= min_coins:
                    min_coins = num_coins
            min_num_coins[money] = min_coins

    # now that our array of min_num_coins is filled out from 0 to money
    # we can just return the required answer

    return min_num_coins[target_money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [1,3,4]
    print(DPChange(m,coins))
