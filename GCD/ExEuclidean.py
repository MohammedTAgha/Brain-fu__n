a = int(input('a :'))
b = int(input('b :'))
temp_a=a
temb_b = b
i = 0
q = a // b
table = []
while True:
    if (i == 0):
        q = a // b
        r = a % b
        s1, s2 = 1, 0
        t1, t2 = 0, 1
        s =s1-(s2 * q)
        t =t1-(t2 * q)
        if(r ==0):
            break
        row = {'q': q, 'a':a ,'b':b , 'r': r , 's1': s1 , 's2':s2 ,'s': s, 't1':t1 ,'t2':t2 ,'t':t}
        a = b
        b = r
        table.append(row)
        # print(i ,row)
    s1, s2 = table[i]['s2'], table[i]['s']
    t1, t2 = table[i]['t2'], table[i]['t']
    if (r != 0):
        q = a // b
        r = a % b
        s = s1 - (s2 * q)
        t = t1 - (t2 * q)
    else:
        break
    row = {'q': q, 'a': a, 'b': b, 'r': r, 's1': s1, 's2': s2, 's': s, 't1': t1, 't2': t2, 't': t}
    a=b
    b=r
    table.append(row)
    i=i+1
for j in table:
    print(j)
print('GCD({},{}) is {} '.format(temp_a,temb_b,table[len(table)-1]['b']) )
print('Bezout coefficients for a and b is {} , {} '.format(table[len(table)-1]['s2'] ,table[len(table)-1]['t2']))
# r =a%b
# row = {'q': q, 'a':a ,'b':b , 'r': a%b , 's1': 1 , 's2':0 ,'s': , 't1': ,'t2': ,'t':}
# print(row)
