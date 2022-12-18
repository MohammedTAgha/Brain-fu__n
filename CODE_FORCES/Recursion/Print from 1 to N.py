x = int(input())


def pr(n):
    if n > x:
        return
    print(n)
    pr(n + 1)


pr(1)
