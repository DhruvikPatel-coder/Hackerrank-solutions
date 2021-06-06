from collections import Counter
from functools import reduce


# noinspection PyGlobalUndefined
def initialize(s):
    # This function is called once before all queries.
    return create_counter(s)


def create_counter(input_string):
    counter_list = [Counter()]
    for element in input_string:
        prev_counter = counter_list[-1]
        counter_list.append(prev_counter + Counter({element: 1}))

    return counter_list


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
pre_comp = []


def answerQuery(left, right, c_list):
    # Return the answer for this query modulo 1000000007.
    freq = c_list[right] - c_list[left - 1]
    return formula(freq)


def factmod(n: int, p: int):
    curr = 1
    res = [1, 1]
    while curr < n:
        curr += 1
        res.append((res[-1] * curr) % p)
        res[-1] %= p
    return res


def lookup(n):
    return pre_comp[n]


def formula(freq: Counter):
    if len(freq.keys()) == 1:
        return 1
    m = list(map(lambda x: x//2, freq.values()))
    s = sum(m)
    factorials = list(map(lookup, m))
    product = prod(factorials)
    result = lookup(s) * pow(product, prime-2, prime)
    count = sum(1 for elem in freq.values() if elem % 2 == 1)
    if count == 0:
        return result % prime
    return (result * count) % prime


def prod(it):
    return reduce(lambda acc, x: acc*x, it, 1)


if __name__ == '__main__':
    prime = 1_000_000_007
    c_list = initialize(input())
    pre_comp = factmod(10 ** 5 // 2, prime)
    no_of_lines = input()
    vals = []
    for i in range(int(no_of_lines)):
        ans = input().split(' ')
        vals.append(answerQuery(int(ans[0]), int(ans[1]), c_list))
    print('\n'.join(map(str, vals)))
