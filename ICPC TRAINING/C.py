cases = int(input())
all = []
for i in range(cases):
    case = input()
    all.append(case)
first = all[0]
second = None
firstcount = 0
for i in all:
    if i == first:
        firstcount += 1
        if i != first:
            second = i
    if i != first:
        second = i
if firstcount > len(all) - firstcount:
    print(first)
else:
    print(second)
