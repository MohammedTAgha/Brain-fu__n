nums = [3,2,4]
target=6
for index, i in enumerate(nums):
    for j in range(0, len(nums)):
        if j == index:
            continue
        if i + nums[j] == target:
            print(index ,j)
            print(nums[j] +i)



