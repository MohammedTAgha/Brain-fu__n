# https://codeforces.com/group/y09sYAnVyp/contest/410315/problem/B

def sol(s):
    if len(s) % 2 != 0:
        return 'NO'
    if (s[0:int(len(s) / 2)] == s[int(len(s) / 2):int(len(s))]):
        return 'YES'
    else:
        return 'NO'


n = int(input())
print()
for i in range(n):
    print(sol(input()))
