a, b = [int(x) for x in input().split()]
def sol(a,b):
    if a==0 and a==0 :
        print("NO")
    elif (a - b == 1 or a - b == -1) or (a==b):
        print("YES")
    else:
        print("NO")
sol(a,b)