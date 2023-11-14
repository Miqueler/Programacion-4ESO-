#A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While

x="s"
sum_total=0
contador=0
while sum_total<50 or sum_total%2==0:
    a=int(input("Introduce el primer número: "))
    b=int(input("Introduce el segundo número: "))
    sum=a+b
    sum_total+=sum
    contador+=1
    print(f"El resultado de la suma es: {sum}")
    if contador == 1:
        print(f"El total acumulado es: {sum_total} y llevas {contador} operación realizada")
    else:
        print(f"El total acumulado es: {sum_total} y llevas {contador} operaciones realizadas")
print("Fin del programa")