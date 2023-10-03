#. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif

let=input("Introduce la letra: ")
if let.isnumeric():
    print("No puede ser un número")
else:
    if  let.islower():
        print("La letra es minúscula")
    elif let.isupper():
        print("La letra es mayúscula")
    elif let.isascii:
        print("El valor introducido es un símbolo")