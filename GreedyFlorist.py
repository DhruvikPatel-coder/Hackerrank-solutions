#!/bin/python3
# Complete the getMinimumCost function below.
import math


def get_minimum_cost(no_of_friends, flowers_cost):
    flowers_cost.sort()
    flowers_to_buy = len(flowers_cost)
    least_buy = flowers_to_buy//no_of_friends
    remaining = ((flowers_to_buy/no_of_friends) - least_buy) * flowers_to_buy
    total = sum(i * least_buy for i in flowers_cost)
    total += sum(flowers_cost[j] for j in range(int(remaining)))
    return total


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    print(get_minimum_cost(k, c))
