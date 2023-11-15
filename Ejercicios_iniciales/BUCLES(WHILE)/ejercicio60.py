#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
x=int(input("Introduce el número del cual quieres la tabla de multiplicar: "))
y=1
while y<11:
    print(x*y)
    y+=1