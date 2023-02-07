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
                    return x
                else:
                    x = n[i]
                    return x
        if n[i] == n[i + 1] and n[i] == n[i + 2]:
            i += 1
            continue
        elif n[i] == n[i + 1] and n[i] != n[i + 2]:
            x = n[i + 2]
            return x
        i += 1


z = [int(x) for x in input().split()]
nc = int
print(sol(z))
