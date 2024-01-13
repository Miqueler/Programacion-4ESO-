keys=[]
while True:
    x=input()
    if x=="#":
        break
    elif x.isnumeric()==True:
        n_keys=int(x)
    else:
        keys.append(x)

for i in range(n_keys):
    temp=keys[0]
    keys.pop(0)
    keys.append(temp)

print(keys)