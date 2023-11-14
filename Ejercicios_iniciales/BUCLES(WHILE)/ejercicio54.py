#Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While

x="s"
sum_total=0
contador=0
while sum_total<50:
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
