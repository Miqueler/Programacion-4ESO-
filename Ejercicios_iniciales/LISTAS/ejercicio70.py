#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

list1=[]
list2=[]
x=int(input("Cuantas palabras quieres introducir?: "))
for i in range(1,x+1):
    y=input(f"Introduce la {i}ª palabra: ")
    list1.append(y)
    list2=[y]+list2

print(list1)
print(list2)