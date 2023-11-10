x=input()
if len(x)<2:
    y=input()
    print(int(y)+int(x))
else:
    l1=x.split()
    print(int(l1[0])+int(l1[1]))