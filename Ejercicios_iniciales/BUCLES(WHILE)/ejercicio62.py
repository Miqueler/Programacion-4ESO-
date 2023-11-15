#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo

a=int(input("Introduce el prinmer número: "))
b=int(input("Introduce el segundo número: "))
pares=""
impares=""
if a>b:
    for i in range(b,a+1):
        if i%2==0:
            pares+=str(i)+"-"
        else:
            impares+=str(i)+"-"
    print(f"los números pares son: {pares[:-1]}")
    print(f"los números impares son: {impares[:-1]}")
elif a<b:
    for i in range(a,b+1):
        if i%2==0:
            pares+=str(i)+"-"
        else:
            impares+=str(i)+"-"
    print(f"los números pares son: {pares[:-1]}")
    print(f"los números impares son: {impares[:-1]}")
