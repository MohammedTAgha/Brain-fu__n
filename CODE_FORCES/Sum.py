# https://codeforces.com/contest/1742/problem/A
def solution(arr):
    arr.sort()
    if arr[len(arr) - 1] == arr[0] + arr[1]:
        print('YES')
    else:
        print('NO')

testcases = int(input())
cases = []
for case in range(testcases):
    x = [int(x) for x in input().split()]
    cases.append(x)
for case in cases:
    solution(case)
