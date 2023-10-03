# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
let=input("Introduce la letra: ")

if  let.islower():
    print("La letra es minúscula")
elif let.isupper():
    print("La letra es mayúscula")
else:
    print("La letra es mayúscula ¿?")
