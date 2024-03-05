import math
try:
    x=float(input())
except ValueError:
    x=int(input())
try:
    if str(x).split(".")[1]=="5": x+=0.1
except:
    pass
print(f"{math.floor(x)} {math.ceil(x)} {int(round(x,0))}")