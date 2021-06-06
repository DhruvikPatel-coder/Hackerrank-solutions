#!/bin/python3
import math
from collections import Counter


# Complete the minTime function below.
def min_time(machines, goal):
    machine_counts = Counter(machines)
    fastest = min(machines)
    min_days = 1
    max_days = math.ceil((fastest*goal)/machine_counts[fastest])
    while max_days - min_days > 1:
        mid = (max_days + min_days)//2
        goods_produced = sum((mid//machine)*count for machine, count in machine_counts.items())
        if goods_produced < goal:
            min_days = mid
        else:
            max_days = mid

    return max_days


if __name__ == '__main__':
    nGoal = input().split()
    n = int(nGoal[0])
    _goal = int(nGoal[1])
    _machines = list(map(int, input().rstrip().split()))
    ans = min_time(_machines, _goal)
    print(ans)
