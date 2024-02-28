from random import randint
with open("VERBOS\diccionario.txt") as d:
    dictionary=d.readlines()

index=randint(0,191)
linea= dictionary[index].split(";")
pasado=linea[1].split(",")
participio=linea[2].split(",")
print(f"El verbo es: {linea[0]}")
print(pasado)
print(participio)