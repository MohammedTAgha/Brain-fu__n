def get_even(array, index):
    if index >= len(array):
        return []
    else:
        x = []
        if index % 2 == 0:
            x = array[index]
            return get_even(array, index + 1) + [array[index]]
        else:
            return get_even(array, index + 1)


input()

x = get_even([int(x) for x in input().split()], 0)
p = [print(x, end=' ') for x in x]
