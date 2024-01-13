names=[]
p_info=[]
n_pyramids=int(input())
for i in range(n_pyramids):
    p_info.append(input())

for i in range(n_pyramids):
    contr=True
    temp=p_info[i]
    pyramid=temp.split()
    name=pyramid[0]; pyramid.pop(0)
    while True:
        if pyramid[0] == "#":
            break
        if pyramid[0] == pyramid[-1]:
            pyramid.pop(0); pyramid.pop(-1)
        else:
            contr=False
            break
    if contr == True:
        print(f"{name} has same number of steps for both faces")
    else:
        print(f"{name} has NOT same number of steps for both faces")