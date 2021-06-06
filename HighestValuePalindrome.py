import math


def highest_value_palindrome(s, n, k):
    # Write your code here
    s = list(s)
    buffer_array = s[::]
    changes_required = calculate(s, n)
    if changes_required > k:
        return '-1'

    if n % 2 == 1:
        j = math.ceil(n / 2)
        for i in range(math.floor(n / 2) - 1, -1, -1):
            if s[i] != s[j]:
                if s[j] > s[i]:
                    s[i] = s[j]
                else:
                    s[j] = s[i]
                changes_required = changes_required - 1
                k = k - 1
            j = j + 1
    else:
        j = int(n / 2)
        for i in range(int(n / 2) - 1, -1, -1):
            if s[i] != s[j]:
                if s[j] > s[i]:
                    s[i] = s[j]
                else:
                    s[j] = s[i]
                changes_required = changes_required - 1
                k = k - 1
            j = j + 1

    s, k = settle_remaining_changes(s, k, buffer_array)
    if k == 1 and n % 2 == 1:
        s[math.floor(n / 2)] = '9'
    return ''.join(s)


def calculate(s, n):
    result = 0
    if n % 2 == 1:
        j = math.ceil(n / 2)
        for i in range(math.floor(n / 2) - 1, -1, -1):
            if s[i] != s[j]:
                result = result + 1
            j = j + 1
    else:
        j = int(n / 2)
        for i in range(int(n / 2) - 1, -1, -1):
            if s[i] != s[j]:
                result = result + 1
            j = j + 1

    return result


def settle_remaining_changes(result_array, remaining_changes, buffer_array):
    j = len(result_array) - 1
    for i in range(0, len(result_array)):
        if result_array[i] < '9':
            if remaining_changes >= 2 and result_array[i] == buffer_array[i] and result_array[j] == buffer_array[j]:
                result_array[i] = result_array[j] = '9'
                remaining_changes = remaining_changes - 2
            elif remaining_changes >= 1 and (result_array[i] != buffer_array[i] or result_array[j] != buffer_array[j]):
                result_array[i] = result_array[j] = '9'
                remaining_changes = remaining_changes - 1
            else:
                break
        j = j - 1
    return result_array, remaining_changes


if __name__ == '__main__':
    answer = input()
    print(highest_value_palindrome(answer, 6, 3))
