x=input()
bisiesto=False
if x[-1]=="0" and x[-2]=="0":
    y=int(x[0]+x[1])
    if y%4==0:
        bisiesto=True
else:
    if int(x)%4==0:
        bisiesto=True
if bisiesto==True:
    print("YES")
else: print("NO")