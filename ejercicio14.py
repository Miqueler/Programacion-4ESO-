#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diametro=float(input("Cuál es el diametro del circulo?: "))
longitud=round(math.pi*diametro,1)
radio=diametro/2
area=round(radio**2*math.pi,1)
print(f"El perimetro del circulo es: {longitud}")
print(f"El área del citculo es: {area}")