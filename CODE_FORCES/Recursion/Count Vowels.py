v = ['a', 'e', 'i', 'o', 'u']
str = input().lower()


def count(str, index):
    if index == len(str):
        return 0
    else:
        if (str[index] in v):
            return 1 + count(str, index + 1)
        else:
            return count(str, index + 1)


print(count(str, 0))
