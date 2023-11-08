# Programa que sume los n primeros números naturales. n Lo introduce el usuario

x=int(input("Introduce el número: "))
suma=0
while x!=0:
    suma+=x
    x-=1
print(f"La suma total de números naturales es: {suma}")
