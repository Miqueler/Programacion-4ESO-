x=int(input())
h,m=0,0
if x>=3600:
    h=x//3600
x-=h*3600
if x>=60:
    m=x//60
x-=m*60
print(f"{h} {m} {x}")