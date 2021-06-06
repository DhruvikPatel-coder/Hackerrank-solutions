#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#
def gridland_metro(n, m, k, track):
    # Write your code here
    spots = n*m
    rows = dict()

    for row in track:
        r = row[0]
        c1 = row[1]
        c2 = row[2]
        if r not in rows:
            rows[r] = [c1, c2]
        else:
            if (c1 > int(rows[r][1]) and c2 > int(rows[r][1])) or (c1 < int(rows[r][0]) and c2 < int(rows[r][0])):
                length = (c2 - c1) + 1
                spots -= length
            else:
                rows[r] = (min(c1, rows[r][0]), max(c2, rows[r][1]))

    for (_c1, _c2) in rows.values():
        length = (_c2 - _c1) + 1
        spots -= length

    return spots


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridland_metro(n, m, k, track)
    print(result)
