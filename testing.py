import random
x=[]
for i in range(1000):
    y=random.randint(1,5)
    if y not in x:
        x.append(y)

print(x)