#Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado=int(input("Cuál es la longitud del cubo?: "))
area=lado**2*6
volumen=lado**3
print(f"El área del cubo es: {area}")
print(f"El volumen del cubo es: {volumen}")