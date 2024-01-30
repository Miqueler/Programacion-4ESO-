#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?

from random import choice
x=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
puntuacion=[]
y=choice(x)
while True:
    point=8
    y=choice(x)
    while True:
        pl=input()
        if pl==y:
            print("ACERTASTE")
            break
        else:
            print("SIGUE JUGANDO")
            point-=1
    puntuacion.append(point)

    if input("Play again? (s/n): ") == "n":
        break
print(f"Puntuación: {puntuacion}")
print(f"Tu puntuación ha sido de {sum(puntuacion)}")
print(f"La media de las partidas realizadas es: {len(puntuacion)*4}")
if len(puntuacion)*4<sum(puntuacion):
    print("Tienes buena suerte")
else:
    print("Dedicate al parchís")
