#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).

from math import sqrt

x=float(input("Introduce el número: "))
raiz=round(sqrt(x), 1)
div=(raiz/2)
print(f"La raíz da: {raiz}")
print(f"La división da: {div.__floor__()}")
