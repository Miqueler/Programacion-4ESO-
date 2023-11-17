#Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos
from random import randint
import time
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0
start_time=time.time()
c_time=0
while c_time-start_time<3:
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
    c_time=time.time()

print(f"Tiempo: {c_time-start_time}")
print(f"Uno: {d1}")
print(f"Dos: {d2}")
print(f"Tres: {d3}")
print(f"Cuatro: {d4}")
print(f"Cinco: {d5}")
print(f"Seis: {d6}")
