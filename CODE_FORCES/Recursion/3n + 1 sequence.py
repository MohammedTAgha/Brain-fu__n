def ulom(n, count):
    if n == 1:
        count += 1
        print(count)
        return None
    if n % 2 == 0:
        count += 1
        n = int(n / 2)
        ulom(n, count)
    else:
        count += 1
        n = int(3 * n + 1)
        ulom(n, count)


x = int(input())
ulom(x, 0)
