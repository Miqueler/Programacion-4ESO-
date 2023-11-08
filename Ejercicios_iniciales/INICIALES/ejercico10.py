#Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
x=float(input("Di un numero: "))
y=float(input("Di un numero: "))
res_co=x/y
resto=x%y
print(f"El cociente es: {res_co}")
print(f"El resto es: {resto}")
if x%2 > 0:
    print("El dividendo es impar")
else:
    print("El dividendo es par")