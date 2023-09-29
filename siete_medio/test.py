text=open("registro.txt","r")
w=0
l=0
d=0
for i in text.read():
    if i=="2":
        w+=1
    if i=="0":
        l+=1
    if i=="1":
        d+=1
print(f"You won {w} times, lost {l} times and drew {d} times")

text.close()