#Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
n=int(input("Introduce la cantidad de números que deseas introducir: "))
cont_p=0
cont_n=0
cont_0=0
for i in range(n):
    x=int(input("Introduce un número: "))
    if x==0:
        cont_0+=1
    elif x>0:
        cont_p+=1
    elif x<0:
        cont_n+=1

print(f"La cantidad de números positivos es: {cont_p}")
print(f"La cantidad de números negativos es: {cont_n}")
print(f"La cantidad de ceros es: {cont_0}")