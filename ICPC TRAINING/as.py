from itertools import permutations

x = int(input())
l = list(permutations(range(0, x)))
print(len(l) - 1)
