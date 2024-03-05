x=input().split()
if int(x[0])>int(x[1]):
    if int(x[0])>int(x[2]):
        print(x[0])
    else: print(x[2])
else: 
    if int(x[1])>int(x[2]):
        print(x[1])
    else: print(x[2])