top = None
results = []

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
        break
print()
print(top)
