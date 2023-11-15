#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.
x=int(input("Introduce el número del cual quieres la tabla de multiplicar: "))
y=1
while x*y<=40:
    print(x*y)
    y+=1
print("Fin del programa")