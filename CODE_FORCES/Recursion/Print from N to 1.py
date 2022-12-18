x = int(input())


def pr(n):
    if n < 1:
        return
    if n == 1:
        print(n, end='')
    else:
        print(n, end=' ')
    pr(n - 1)


pr(x)
