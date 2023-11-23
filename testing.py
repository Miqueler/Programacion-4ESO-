x=[[2,3],[1]]
for i in x:
    if 2 in i:
        i.pop(i.index(2))
print(x)