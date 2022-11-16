l1 = [2,4,3]
l2 = [5,6,4]
r1 = [3,4,2]
r2 = [4,6,5]
l1.reverse()
l2.reverse()
sum1 , sum2 = 0 ,0
for i , x  in enumerate(l1):
    sum1=sum1 + (x* (10**(len(l1) -1 - i)) )
for i , x  in enumerate(l2):
    sum2=sum2 + (x* (10**(len(l1) -1 - i)) )
sum=list(str(sum1+sum2))
for i , x in enumerate(sum):
    sum[i]=int(x)
print(sum[::-1])



