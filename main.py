import math

n = int(input())
x = math.sqrt(n)
y = int(x)
if (x - y == 0):
    print('YES')
else:
    print('NO')

print(math.sqrt(n) - int(n))
