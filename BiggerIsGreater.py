def bigger_is_greater(w):
    w = list(w)
    # Find non-increasing suffix
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    # Find the rightmost successor to pivot in the suffix
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    # Swap the pivot with the rightmost character
    w[i - 1], w[j] = w[j], w[i - 1]

    # Reverse the suffix
    w[i:] = w[:i-1:-1]

    return ''.join(w)


if __name__ == '__main__':
    print(bigger_is_greater("abcfdda"))
