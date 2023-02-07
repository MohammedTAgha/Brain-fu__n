s = input()
s1 = s[0]
n = len(s)
i = 1
f = 0
while i < n:
    if i < n - 3 and s[i:i + 3] == "dot":
        s1 = s1 + "."
        i += 3
    elif s[i:i + 2] == "at" and f == 0:
        s1 = s1 + "@"
        i += 2
        f = 1
    else:
        s1 = s1 + s[i]
        i += 1
print(s1)
