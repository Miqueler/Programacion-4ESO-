#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
from random import choice
x=["1","2"]
y=choice(x)
while True:
    pl=input()
    if pl==y:
        print("ACERTASTE")
        break
    else:
        print("SIGUE JUGANDO")