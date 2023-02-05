# https://codeforces.com/contest/1791/problem/A

codeforces = 'codeforces'
n = int(input())
x = []
for i in range(n):
    x.append(input())
for i in x:
    if i in codeforces:
        print("yes")
    else:
        print('no')
