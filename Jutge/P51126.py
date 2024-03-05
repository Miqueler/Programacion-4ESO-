x=input().split()
a1,b1,a2,b2=int(x[0]),int(x[1]),int(x[2]),int(x[3])
if b1<a2 or b2<a1:
    print("[]")
else:
    fin=[]
    fin.append(max(a1,a2))
    fin.append(min(b1,b2))
    print(f"[{fin[0]},{fin[1]}]")