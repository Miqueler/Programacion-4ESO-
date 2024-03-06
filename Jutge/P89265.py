x=input().split()
w="?"
if int(x[0])==int(x[2]) and int(x[1])==int(x[3]):
    w="="
elif int(x[0])>=int(x[2]) and int(x[1])<=int(x[3]):
    w="1"
elif int(x[0])<=int(x[2]) and int(x[1])>=int(x[3]):
    w="2"
a1,b1,a2,b2=int(x[0]),int(x[1]),int(x[2]),int(x[3])
if b1<a2 or b2<a1:
    print(f"{w} , []")
else:
    fin=[]
    fin.append(max(a1,a2))
    fin.append(min(b1,b2))
    print(f"{w} , [{fin[0]},{fin[1]}]")