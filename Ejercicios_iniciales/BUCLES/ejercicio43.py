#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra

x=input("Introduce una palabra: ")
for i in range(len(x)):
    print(f"En la posición {i} está la {x[i]}")