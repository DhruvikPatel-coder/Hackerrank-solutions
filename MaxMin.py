#!/bin/python3
#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
import math


def max_min(dt, array):
    unfair = math.inf
    # Write your code here
    array.sort()
    for i in range(0, len(array) - dt + 1):
        unfair = min(unfair, array[i + dt - 1] - array[i])

    return unfair


if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = max_min(k, arr)
    print(result)
