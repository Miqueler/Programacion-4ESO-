x=input()
y=""
vocales=["a","e","i","o","u"]
for i in x:
    if i.lower() in vocales:
        y+="*"
    else:
        y+=i
print(y)