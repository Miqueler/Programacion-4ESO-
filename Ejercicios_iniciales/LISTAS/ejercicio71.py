#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.

total=[]
x=int(input("Cuántos números quieres introducir?: "))
for i in range(x):
    test=True
    while test:
        y=input("Introduce un número: ")
        if y not in total and y.isnumeric()==False:
            test=False
    
    total.append(y)

print(total)    