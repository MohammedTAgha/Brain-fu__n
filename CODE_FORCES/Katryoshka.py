# https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/G

e = 0
m = 222
b = 322

def sol(e, m, b):
    count = 0
    while True:
        if e <= 0 and b == 0:
            break
        if e >= 1 and m >= 1 and b >= 1:
            if(e>m and b>m):
                count +=m
                e -= m
                b -= m
                m -= m
            else:
                count += 1
                e -= 1
                b -= 1
                m -= 1
        elif e >= 2 and b >= 1:
            count += 1
            e -= 2
            b -= 1

        elif e >= 2 and m >= 1 and b >= 1:
            count += 1
            e -= 2
            b -= 1
            m -= 1
        else:
            break
    return count

e, m, b = [int(x) for x in input().split()]
print(sol(e, m, b))
