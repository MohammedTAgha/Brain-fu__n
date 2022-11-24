results = []


def findTop(case):
    top = None
    for i in range(8):
        x = input()
        for j in range(len(x) - 1):
            # if x[j] =='.':
            #     continue
            if x[j] == 'B':
                top = 'B'
            elif x[j] == 'R' and x[j + 1] == 'R':
                top = 'R'
            elif x[j] == 'R' and x[j + 1] == 'B':
                top = 'B'
        if top == 'R':
            results.append(top)
            return top
            break
    results.append(top)
    return top


ntests = int(input())
cases = []
for n in range(ntests):
    case = input()
    cases.append(findTop(case))
print()
for r in results:
    print(r)
