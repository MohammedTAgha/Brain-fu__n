results = []


def findTop(case):
    top = None
    for i in range(8):
        x = input()
        for j in range(len(x) - 1):

            if x[j] == 'R' and x[j + 1] == 'R':
                top = 'R'
            elif x[j] == 'R' and x[j + 1] == 'B':
                top = 'B'
            elif x[j] == 'B':
                top = 'B'
        if top == 'R':
            results.append(top)
            print('>>',top)
            return top
            break
    results.append(top)
    print('>>', top)

    return top


ntests = int(input())
cases = []
for n in range(ntests):
    case = input()
    x = findTop(case)
    cases.append(x)
print()
for r in results:
    print(r)
