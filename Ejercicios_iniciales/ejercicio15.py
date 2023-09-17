#Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
from math import pi

radio=float(input("Cuál es el radio del cilindro?: "))
altura=float(input("Cuál es la altura del cilindro?: "))

area=round(2*pi*radio*altura+2*pi*radio**2, 2)
vol=round(radio**2*pi*altura, 2)
print(f"El área del cilindro es: {area}")
print(f"El volumen del cilindro es: {vol}")
print(2*3*4*5+1*2*3**2)