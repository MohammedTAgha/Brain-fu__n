def sum(a, i, m):
    if i < (len(a) - m):
        return 0
    else:
        return a[i] + sum(a, i - 1, m)


n, m = [int(b) for b in input().split()]
arr = [int(x) for x in input().split()]
print(sum(arr, len(arr) - 1, m))
