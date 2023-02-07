s1 = input()
s2 = input()
IS_FLIPPED = False
for i in range(0, len(s1)):
    if (len(s1) != len(s2)):
        print('NO')
        break
    if (s1[i] == s2[len(s1) - 1 - i]):
        IS_FLIPPED = True
    else:
        print('NO')
        IS_FLIPPED = False
        break
if (IS_FLIPPED):
    print('YES')
