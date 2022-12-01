
def exGCD(a ,b ):
    temp_a = a
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
            s = s1 - (s2 * q)
            t = t1 - (t2 * q)
            if (r == 0):
                break
            row = {'q': q, 'a': a, 'b': b, 'r': r, 's1': s1, 's2': s2, 's': s, 't1': t1, 't2': t2, 't': t}
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
        a = b
        b = r
        table.append(row)
        i = i + 1

    print('    q    |    a    |    b    |    r    |    s1   |    s2   |    s    |    t1   |    t2   |    t    |')
    for j in table:
        print('{:<9}|{:<9}|{:<9}|{:<9}|{:<9}|{:<9}|{:<9}|{:<9}|{:<9}|{:<9}'.format(j['q'], j['a'], j['b'], j['r'],
                                                                                   j['s1'], j['s2'], j['s'], j['t'],
                                                                                   j['t1'], j['t']))
    print('GCD({},{}) is {} '.format(temp_a, temb_b, table[len(table) - 1]['b']))
    print(
        'Bezout coefficients for a and b is {} , {} '.format(table[len(table) - 1]['s2'],
                                                             table[len(table) - 1]['t2']))
    return {'gcd':table[len(table) - 1]['b'],'s':table[len(table) - 1]['s2']}

while True:
    x = exGCD(int(input('a :')),int(input('b :')))
    if x['gcd'] ==1 :
        print('THAY ARE RELETIVLY PRIME')
    print('******')
