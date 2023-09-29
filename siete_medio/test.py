text=open("registro.txt","r")
w=0
l=0
d=0
tg=0
for i in text.read():
    if i=="2":
        w+=1
    if i=="0":
        l+=1
    if i=="1":
        d+=1
tg=w+l+d
pw=round(w/tg*100,2)
pl=round(l/tg*100,2)
pd=round(d/tg*100,2)

print(f"You won {w} times, lost {l} times and drew {d} times")
print(f"You won {pw}% of times, lost {pl}% of times and drew {pd}% of times")
text.close()