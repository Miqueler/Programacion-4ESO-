x=input().split()
y=[]
for i in x:
    y.append(i)
x.sort()
if x[0]==x[1]:print(f"{y[0]} = {y[1]}")
elif x[0]==y[0]:
    print(f"{y[0]} < {y[1]}")
else: print(f"{y[0]} > {y[1]}") 