x=input()
l1=0
if len(x.split())==2:
    y=input()
    for i in x.split():
        l1+=int(i)
    print(int(y)+int(l1))
else:
    for i in x.split():
        l1+=int(i)
    print(l1)