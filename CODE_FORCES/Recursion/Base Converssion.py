reversed = []


def f(n):
    if n == 0:
        return
    q = n // 2
    r = n % 2
    reversed.append(r)
    f(q)


n = int(input())
cases = []
for i in range(n):
    cases.append(int(input()))
for num in cases:
    f(num)
    reversed.reverse()
    p = [print(x, end='') for x in reversed]
    reversed = []
    print()

# while True :
#     if n ==0 :
#         break
#     q=n // 2
#     r= n%2
#     reversed.append(r)
#     n=q
