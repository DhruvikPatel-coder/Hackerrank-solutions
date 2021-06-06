#!/bin/python3
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def array_manipulation(number_of_elements, queries):
    # Write your code here
    array = [0 for _ in range(number_of_elements + 1)]
    for q in queries:
        i, j, to_add = q[0], q[1], q[2]
        sum_of_elements(array, i - 1, j, to_add)
    arrSum = 0
    maxSum = 0
    for i in range(len(array)):
        arrSum += array[i]
        maxSum = max(maxSum, arrSum)
    return maxSum


def sum_of_elements(array, start, end, number):
    array[start] = array[start] + number
    array[end] = array[end] - number
    return array


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    query = []
    for _ in range(m):
        query.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, query)
    print(result)
