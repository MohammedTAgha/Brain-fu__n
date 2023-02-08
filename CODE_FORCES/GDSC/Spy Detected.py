# https://codeforces.com/group/y09sYAnVyp/contest/410315/problem/A

def sol(n):
    i = 0
    x = None
    while True:
        if (i >= len(n) - 2):
            break
        if n[i] != n[i + 1]:
            if i == 0:
                if n[i] == n[i + 2]:
                    x = n[i + 1]
                    return i + 2
                else:
                    x = n[i]
                    return i + 1
        if n[i] == n[i + 1] and n[i] == n[i + 2]:
            i += 2
            continue
        elif n[i] == n[i + 1] and n[i] != n[i + 2]:
            x = n[i + 2]
            return i + 3
        i += 1


cases = []
nc = int(input())
for j in range(nc):
    s = input()
    z = [int(x) for x in input().split()]
    cases.append(z)
for k in cases:
    print(sol(k))
