#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
from random import randint
r_num=randint(1,5)
guess=0
while guess!=r_num:
    guess=0
    while guess >5 or guess< 1:
        guess=int(input("Introduce el número (1-5): "))
    if guess!=r_num:
        print("Número equivocado")
print("Número correcto")