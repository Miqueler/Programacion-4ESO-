# Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.

total=[]
x=int(input("Cuántos números quieres introducir?: "))
for i in range(x):
    y=int(input("Introduce un número: "))
    total.append(y)

print(total)