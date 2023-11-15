#Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número
from random import randint
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0

for i in range(100):
    r_dice=randint(1,6)
    if r_dice==1:
        d1+=1
    elif r_dice==2:
        d2+=1
    elif r_dice==3:
        d3+=1
    elif r_dice==4:
        d4+=1
    elif r_dice==5:
        d5+=1
    elif r_dice==6:
        d6+=1
print(f"Uno: {d1}")
print(f"Dos: {d2}")
print(f"Tres: {d3}")
print(f"Cuatro: {d4}")
print(f"Cinco: {d5}")
print(f"Seis: {d6}")
