# Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos

from random import randint
r_num=randint(1,1000)
guess=0
counter=0
print(r_num)
while guess != r_num:
    guess=int(input("Introduce un valo entre el 1 y el 1000: "))
    if guess > r_num:
        print("El número a adivinar és menor")
    elif guess < r_num:
        print("El número a adivinar és mayor")
    counter+=1
print(f"Correcto!, has tardado {counter} intentos")