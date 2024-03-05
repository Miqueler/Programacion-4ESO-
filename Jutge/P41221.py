all_list=[]
while len(all_list) !=3:
    x=input().split()
    for i in x:
        all_list.append(i)
res=0
for i in all_list:
    res+=int(i)
print(res)