# https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/I
def check_divisbilty(a, b):
    if a % b == 0 or b % a == 0:
        print("YES")
        return True
    else:
        print("NO")
        return False


n = int(input())
check_divisbilty(n % 10, n // 10)
