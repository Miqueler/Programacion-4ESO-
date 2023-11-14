#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
x="s"
sum_total=0
contador=0
while x=="s":
    a=int(input("Introduce el primer número: "))
    b=int(input("Introduce el segundo número: "))
    sum=a+b
    print(f"El resultado de la suma es: {sum}")
    sum_total+=sum
    contador+=1
    x=input("Deseas repetir la operación s/n: ")
print("Resumen: ")
print(f"la suma total es: {sum_total} y el número de repeticiones es: {contador}")