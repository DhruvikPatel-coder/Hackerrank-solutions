import math


def encryption(s):
    # Write your code here
    ans = []
    s = s.replace(" ", "")
    s = list(s)
    row_length = math.ceil(math.sqrt(len(s)))
    for i in range(0, row_length):
        for j in range(i, len(s), row_length):
            ans.append(s[j])
        ans.append(" ")
    return ''.join(ans)


if __name__ == '__main__':
    print(encryption("have a nice day"))
