rows = int(input())


def row(n):
    if (n == rows):
        return
    s = (rows - n) - 1
    x = (n * 2) + 1
    print(' ' * s, end='')
    print('*' * x)
    row(n + 1)


row(0)
