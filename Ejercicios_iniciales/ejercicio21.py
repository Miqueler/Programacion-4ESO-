#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
from math import sqrt
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if b**2-4*a*c>0:
    res_ma=(-b+sqrt(b**2-4*a*c))/(2*a)
    res_me=(-b-sqrt(b**2-4*a*c))/(2*a)
    print(f'''The first result is: {res_ma}
The second result is: {res_me}''')
else: 
    print("The square root mustn't be negative")