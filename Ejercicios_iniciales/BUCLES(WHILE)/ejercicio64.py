#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos

x=0
par=0
impar=0
pos=0
neg=0
cer=0
sum_total=0
while x!=-99:
    x=int(input("Introduce un número: "))
    if x==0:
        pass
    elif x%2==0:
        par+=1
    else:
        impar+=1

    if x==0:
        cer+=1    
    elif x>0:
        pos+=1
    else:
        neg+=1
    sum_total+=x
sum_total+=99
print(f'''RESUMEN
El número de pares es {par}
El número de impares es {impar}
El número de positivos es {pos}
El número de negativos es {neg}
El número de ceros es {cer}
El total es {sum_total}''')