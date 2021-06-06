import sys
from collections import Counter


#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def abbreviation(string_a, string_b, count_a, count_b):
    # Write your code here
    count_a_used = [Counter()]
    count_b_used = [Counter()]
    if len(string_a) < len(string_b):
        return "NO"
    if len(string_a) == len(string_b) and string_a.upper() != string_b.upper():
        return "NO"

    i = 0
    j = 0
    while i < len(string_a) and j < len(string_b):
        if string_a[i] == string_b[j]:
            update_counter(string_a, string_b, i, j, count_a_used, count_b_used)
            j += 1
        elif string_a[i].islower():
            first_char_a = string_a[i].upper()
            first_char_b = string_b[j]
            if first_char_a == first_char_b:
                latest_counter_a = count_a_used[-1]
                latest_counter_b = count_b_used[-1]
                char_a_used = latest_counter_a[first_char_a] + latest_counter_a[string_a[i]]
                char_b_used = latest_counter_b[first_char_b]
                if count_a[i][first_char_a] - char_a_used < count_b[j][first_char_b] - char_b_used:
                    update_counter(string_a, string_b, i, j, count_a_used, count_b_used)
                    j += 1
        elif string_a[i].isupper():
            break
        i += 1

    if len(string_b) == j:
        return "YES" if i == len(string_a) or string_a[i:].islower() else "NO"
    else:
        return "NO"


def update_counter(string_a, string_b, i, j, count_a_used, count_b_used):
    prev_a = count_a_used[-1]
    count_a_used.append(prev_a + Counter({string_a[i]: 1}))
    prev_b = count_b_used[-1]
    count_b_used.append(prev_b + Counter({string_b[j]: 1}))
    return count_a_used, count_b_used


def create_counter(input_string):
    counter_list = [Counter(input_string)]
    for element in input_string:
        prev_counter = counter_list[-1]
        counter_list.append(prev_counter - Counter({element: 1}))

    return counter_list


if __name__ == '__main__':
    sys.setrecursionlimit(1100)
    q = int(input().strip())
    for q_itr in range(q):
        a = input()
        b = input()

        counter_a = create_counter(a)
        counter_b = create_counter(b)
        print(abbreviation(a, b, counter_a, counter_b))
