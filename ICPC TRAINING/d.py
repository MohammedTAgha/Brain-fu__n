n = input()
n7, n4 = 0, 0

for i in n:
    if i == '4':
        n4 += 1
    elif i == '7':
        n7 += 1
if n7 == 0 and n4 == 0:
    print(-1)
elif n7 == n4:
    print(4)
elif n7 > n4:
    print(7)
elif n4 > n7:
    print(4)

# print(n4,n7)
