x=input().split()
h,m,s=int(x[0]),int(x[1]),int(x[2])
s+=1

if s>=60:
    m+=1
    s="00"
if m>=60:
    h+=1
    m="00"
if h>=24:
    h="00"
if int(s)<10 and s!="00": s=f"0{s}"
if int(m)<10 and m!="00": m=f"0{m}"
if int(h)<10 and h!="00": h=f"0{h}"
print(f"{h}:{m}:{s}")