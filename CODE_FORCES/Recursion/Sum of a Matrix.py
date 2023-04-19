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
print(m1)
print(m2)
z = [[1, 2, 3], [4, 5, 6]]


def sum(m, i, j):
    if (i == 0 and j == 0):
        return m[i][j]
    if j == 0:
        return sum(m, i - 1, len(m[0]) - 1) + m[i][j]
    return sum(m, i, j - 1) + m[i][j]


print(sum(m1, r - 1, c - 1) + sum(m2, r - 1, c - 1))
