#Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla

let=input("Introduce la letra: ")
if let.isnumeric():
    print("No puede ser un número")
else:
    if  let.islower():
        print("La letra es minúscula")
    elif let.isupper():
        print("La letra es mayúscula")
    else:
        print("La letra es mayúscula ¿?")