#Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif

x=input("Introduce un texto: ")
longitud=len(x)
if longitud==11:
    print("La frase tiene 11 caracteres")
elif longitud>11:
    print("La frase tiene más de 11 caracteres")
elif longitud<11:
    print("La frase tiene menos de 11 caracteres")
