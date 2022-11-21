def solution(l, k):
    res=[]
    for i in l :
        if i !=k :
            res.append(i)
    return res
print(solution([3, 1, 2, 3, 4, 5],3))