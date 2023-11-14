#Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
x="s"
while x=="s":
    a=int(input("Introduce el primer número: "))
    b=int(input("Introduce el segundo número: "))
    print(f"El resultado de la suma es: {a+b}")
    x=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")
