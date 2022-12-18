def pr(n):
    if n == 0:
        return
    print('I love Recursion')
    pr(n - 1)


n = int(input())
pr(n)
