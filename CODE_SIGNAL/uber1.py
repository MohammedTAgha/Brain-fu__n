def solution(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    print()
    # (Cost per minute) * (ride time) + (Cost per mile) * (ride distance)
    fare=[]
    for i in range(len(cost_per_minute)):
        total=(cost_per_minute[i] * ride_time ) + (cost_per_mile[i]*ride_distance)
        fare.append(total)
    return (fare)
print(solution(30 , 7 ,[0.2, 0.35, 0.4, 0.45] , [1.1, 1.8, 2.3, 3.5]))
