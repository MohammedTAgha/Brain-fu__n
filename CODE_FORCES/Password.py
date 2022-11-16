# https://codeforces.com/contest/1743/problem/A

list=[3,7]
list2=[3,3,7,7]

def tow_digits(d1 ,d2):
    list1 = [d1 , d2 ]
    list2 = [d1, d1 , d2 ,d2]
    copy=list2
    all = []

    def swap(n1, n2):
        temp = list2[n1]
        list2[n1] = list2[n2]
        list2[n2] = temp
        return list2
    for i in range(0, len(list2)):
        list2 = [d1, d1 , d2 ,d2]
        for j in range(0, len(list2)):
            temp = list2[i]
            list2[i] = list2[j]
            list2[j] = temp
            # x=swap(j , i)
            # print(list2, end='')
            list2 =[d1, d1 , d2 ,d2]
            all.append(list2)
        # print()
    filtered = []
    for password in all:
        if password not in filtered:
            filtered.append(password)
    # print(filtered)
    # print(len(all))
    # print(len(filtered))
    return all
def find_copm(a , b):
    t1 = tow_digits(a, b)
    t2 = tow_digits(b, a)
    total = [*t1, *t2]
    clear = []
    for password in total:
        if password not in clear:
            clear.append(password)
    return clear
# find_copm(3,7)
def all_possible(l):
    n = [x for x in range(0, 10)]
    list = []
    for remembers in n:
        if remembers in l:
            continue
        list.append(remembers)
    sum=0
    for i in range(0 , len(list)):
        for k in range(0 , len(list)):
            if i == k :
                continue
            sum = sum+ len(find_copm(i , k))
    return int(sum/2)
allcases=[]
testcases = int(input())
for case in range(testcases):
    z=input()
    x = [int(x) for x in input().split()]
    allcases.append(x)
for i in allcases:
    print(all_possible(i))
# for test in range(0,testcases):
#     case = input().split()


# print(all_possible([8]))