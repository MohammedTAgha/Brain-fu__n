n=5
h=60

a=18
b=2

points={0:0 ,
        20 :20,
        30 :10,
        50 :30,
        70 :20
        }
all_hights= points.copy()
for i in points:
        # print(i , 60 -points[i] )
        all_hights[i] =60 -points[i]
print(all_hights)
for j in all_hights:
        if j ==list(all_hights)[-1] or j ==list(all_hights)[0]:
                continue
        print(j ,all_hights[j] )

# list(all_hights)[-1]

# check validation
# for
# print(points)
