# https://app.codesignal.com/interview-practice/question/PLCrGrJmBxQdj8QKX/description

a=[9, 6, 4, 2, 3, 5, 7, 0, 1]
def solution(arr):
    l =sorted(arr)
    found_missing=False
    if l[0] != 0:
        found_missing=0
        return found_missing
    for i in range(0 ,len(l)-1):
        if l[i]+1 != l[i+1]:
            found_missing=l[i]+1
            return found_missing
    else:
        if found_missing ==False:
            found_missing=l[len(l)-1]+1
            return found_missing
print(solution(a))