num=int(input())
flag=False
if num==1:
    flag=True
else:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
rev_flag=False
if flag==False:
    