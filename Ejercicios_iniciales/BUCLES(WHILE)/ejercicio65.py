#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor

x=int()
max=int()
min=int()

while x!=-99:
    x=int(input("Introduce un número: "))
    if x==-99:
        pass
    elif x>max:
        max=x
    elif x<min:
        min=x

print(f'''RESUMEN
El número de mayor es {max}
El número de menor es {min}''')