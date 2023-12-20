x=input("").split()
rev_x=[]
fin=""
for i in x:
    rev_x=[i]+rev_x
for i in rev_x:
    fin+=str(i)+" "
print(fin[:-1])