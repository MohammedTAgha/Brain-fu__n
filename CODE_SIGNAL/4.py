# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

def solution(inputArray):
    sum =inputArray[0]*inputArray[1]
    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1]>sum:
            sum=inputArray[i] * inputArray[i+1]
    return sum





test=[5, 6, -4, 2, 3, 2, -23]
print(solution([4, 1, 2, 3, 1, 5]))
# print(solution())
# if(s[0]<0):
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if i == j :
#                     continue
#                 if s[j]>0 and s[i]>0:
#                     break
#                 if s[i] * s[j] > sum:
#                     sum=s[i] * s[j]
#     return sum