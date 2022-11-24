# https://codeforces.com/contest/1742/problem/B

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def sol(list):
    list.sort()
    for i in range(1, len(list)):
        if list[i - 1] == list[i]:
            print('NO')
            break
    else:
        print('YES')


testcases = int(input())
cases = []
for case in range(testcases):
    input()
    x = [int(x) for x in input().split()]
    cases.append(x)
for case in cases:
    sol(case)
