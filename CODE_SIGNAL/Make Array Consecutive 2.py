
# a= [6, 3]
# a.sort()
# s = 0
#
# print()
# s = 0
# def solution(a):
#     a.sort()
#
#     def check(n):
#         global s
#         if (n > 0):
#             s = s + ((a[n] - a[n - 1])) - 1
#             return check(n - 1)
#         else:
#             return s
#     return check(len(a) - 1)
# print(solution([6, 3]))

s = 0
def solution(a):
    a.sort()

    def check(n):
        global s
        if (n > 0):
            s = s + ((a[n] - a[n - 1])) - 1
            return check(n - 1)
        else:
            return s
    return(check(len(a) - 1))
print(solution([6, 3]))




# other solutions