# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/K

n, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(x):
    last = a[len(a) - 1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last
for i in a:
    print(i, end=" ")
