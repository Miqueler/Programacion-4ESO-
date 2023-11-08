#programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
x=int(input("Da un numero: "))
y=int(input("Da un numero: "))
res1=x+y
res2=x-y
res3=x*y
res4=x/y
res4fin=round(res4, 2)
res5=x**y
res6=x//y
print(f"La suma del numero1 y numero2 es: {res1}")
print(f"La resta del numero1 y numero2 es: {res2}")
print(f"La multiplicación del numero1 y numero2 es: {res3}")
print(f"La division del numero1 y numero2 es: {res4fin}")
print(f"El exponente del numero1 y numero2 es: {res5}")
print(f"La división entera de numero1 y numero2 es: {res6}")