#!/bin/python3
import math
from collections import OrderedDict


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def two_pluses(grid):
    # Write your code here
    rows = len(grid)
    cols = len(grid[0])
    res = list()
    for z in grid:
        res.append(list(z))
    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = two_pluses(grid)
    print(result)
