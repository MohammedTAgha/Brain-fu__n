a , b = 900 ,750
a1=a
b1=b
q , r=None ,None
print(' q  ||  a   ||  b   || r  ')
while True :
    q = a // b
    r = a % b
    print('{:<4}|| {:<4} || {:<4} || {:<4} '.format(q, a, b, r))
    a=b
    b=r
    if (r==0):
        print('    || {:<4} || {:<4} ||   '.format( a, b))
        print('**********************')
        print ('GCD({} , {}) is {} '.format( a1 , b1 , a))
        break
