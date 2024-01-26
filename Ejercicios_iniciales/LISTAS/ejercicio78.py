#A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
while True:
    x=input("Introduce el valor que deseas eliminar: ")
    if x.isnumeric():
        try:    
            lista1.pop(lista1.index(x))           
        except ValueError:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce valor numérico")
    y=input("Deseas introducir otro valor s/n: ")
    if y=="n":
        break