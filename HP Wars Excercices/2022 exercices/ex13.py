from math import ceil
x=input()
abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
total=int()
if x.isnumeric():
    fin=""
    if int(x)<=26:
        print(abc[int(x)-1])
    else: 
        x=int(x)
        div=x/26
else:
    if len(x)==1:
        print(abc.index(x)+1)
    else:
        for i in range(len(x)):
            f=i+1
            total+=(abc.index(x[i])+1)*26**(len(x)-f)
        print(total)