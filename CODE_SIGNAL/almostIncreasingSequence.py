# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

a=[1, 3, 2, 1]
incr=True
delCount=0
for i in range(len(a)-1 , 0 ,-1):
    print(a[i]," ---- ",a[i-1])
    if a[i]-a[i-1]<=0:#if num not grater than before it
        incr=False
        delCount +=1
print(delCount)
print(incr)