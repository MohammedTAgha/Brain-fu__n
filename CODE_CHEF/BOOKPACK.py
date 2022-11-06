n = int(input())
cases=[]
for i in range(n):
    test = input().split()
    cases.append(test)
for i in cases:
    rows=int(i[0])
    row=int(i[1])
    box=int(i[2])
    eachrow=row//box
    rem=0
    if row%box !=0:
        rem=1
    total = (eachrow + rem) * rows
    print(total)