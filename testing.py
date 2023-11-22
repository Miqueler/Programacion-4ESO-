x=[[2],[1]]
print(x.__len__())
x.pop([0][0])
print(x.__len__())
print(x)

x=[[2],[1]]
if 2 in x[0]:
    print("True")