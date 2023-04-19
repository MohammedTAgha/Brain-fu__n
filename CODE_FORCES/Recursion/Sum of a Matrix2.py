m1 = []
m2 = []
r, c = [int(b) for b in input().split()]
for row in range(0, r * 2):
    if row < r:
        x = [int(b) for b in input().split()]
        m1.append(x)
    else:
        x = [int(b) for b in input().split()]
        m2.append(x)


def sum(m, mm, i, j):
    if (i == r - 1 and j == c - 1):

        return m[i][j] + mm[i][j]
    else:
        print(m[i][j] + mm[i][j], end=" ")
    if j == c - 1:
        print()
        return sum(m1, m2, i + 1, 0)
    return sum(m1, m2, i, j + 1)


if r == 0 or c == 0:
    print(0)
print(sum(m1, m2, 0, 0))
