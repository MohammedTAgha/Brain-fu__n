def get_sum(array, index):
    if index == 0:
        return array[0]
    else:
        return array[index] + get_sum(array, index - 1)


input()
z = [int(x) for x in input().split()]
print(get_sum(z, len(z) - 1))
# x= get_sum(, 0)
# p = [print(x, end=' ') for x in x]
