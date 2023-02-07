x = input()
if x[0:2] == 'at' or x[0:3] == 'dot':
    a = x[2:-2].replace('dot', '.')
    b = a.replace('at', "@", 1)
    print('{}{}{}'.format(x[0:2], b, x[-2:]))
else:
    a = x.replace('dot', '.')
    b = a.replace('at', "@", 1)
    print(b)
