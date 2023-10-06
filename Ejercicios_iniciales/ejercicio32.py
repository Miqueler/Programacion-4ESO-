#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas

a="A quién madruga Dios ayuda"
z=input("Itroduce un texto: ")
y=z.lower()
x=a.lower()
existe=x.find(y)

if existe != -1:
    print(f"La palabra está en la frase y está en el índice {existe}")
else: 
    print("La palabra no está en la frase")