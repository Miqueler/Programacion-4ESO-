#Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
x=input().split(".")
if len(x)==1:
    print("No es un número con decimales")
elif len(x)==2:
    print("Es un número con decimales")
else:
    print("No es un número con decimales")
