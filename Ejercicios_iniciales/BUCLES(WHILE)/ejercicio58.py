#Modifica el programa anterior para que tengas 3 intentos. Utiliza while
from random import randint
r_num=randint(1,5)
guess=0
counter=3
while counter!=0 and guess!=r_num:
    guess=0
    while guess >5 or guess< 1:
        guess=int(input("Introduce el número (1-5): "))
    if guess!=r_num:
        print("Número equivocado")
    counter-=1
if guess==r_num:
    print("Número correcto")
else:
    print("Te has quedado sin intentos")