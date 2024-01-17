nums=input().split()
friends=0
for i in range(9):
    for x in range(9):
        if nums[x]==i+1:
            friends+=1
for i in range(9):
    for x in range(9):
        if nums[x*9]==i+1:
            friends+=1
for i in range(9):
    for x in range(9):
        for y in range(3):
            if nums[x*(y+1)]==i:
                friends+=1
print(friends)