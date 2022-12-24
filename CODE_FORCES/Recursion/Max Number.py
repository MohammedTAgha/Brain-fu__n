# def find_max_recursive(arr):
#   if len(arr) == 1:
#     return arr[0]
#   max_of_rest = find_max_recursive(arr[1:])
#   return max(arr[0], max_of_rest)
# m = float('-inf')
#
# print(1 < m)
# a = [1, -3, 5, 4, -6]
#
#
# def max(a, i):
#     if i < len(a):
#         if a[i] > max(a, i + 1):
#             return a[i]
a, b = [int(x) for x in input().split()]
print(a+b)