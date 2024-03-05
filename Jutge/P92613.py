import math
try:
    x=float(input())
except ValueError:
    x=int(input())
if str(x).split(".")[2]=="5": x+=0.1
print(f"{math.floor(x)} {math.ceil(x)} {int(round(x,0))}")