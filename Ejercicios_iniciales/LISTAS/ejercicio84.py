#. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra
from random import choice, shuffle
x=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
y=choice(x)
z=list(y)
shuffle(z)
final_word="".join(z)
counter=3
print(final_word)
win=False
while counter!=0:
    player=input("Introduce la palabra correta: ")
    if player==y:
        win=True
        counter=0
        print("Has acertado")
    else:
        print("No has acertado")
        counter-=1
if win==False:
    print("No has acertado ninguno de los intentos")