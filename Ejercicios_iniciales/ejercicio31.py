#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.
x="A quién madruga Dios ayuda"
y=input("Itroduce un texto: ")

existe=x.find(y)

if existe != -1:
    print(f"La palabra está en la frase y está en el índice {existe}")
else: 
    print("La palabra no está en la frase")