#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista

total=[]
acentos={"à": "a","á":"a","è":"e","é":"e","ì":"i","í":"i","ò":"o","ó":"o","ù":"u","ú":"u"}
vocales=["a","e","i","o","u"]
temp=""
x=int(input("Cuántos caracteres quieres introducir?: "))
for i in range(x):
    test=True
    while test:
        y=input("Introduce un número: ")

        if y in acentos and y not in vocales:
            temp=acentos[y]
            if temp not in total:
                print("K")
        elif y not in total and y.isnumeric()==False:
            test=False
    
    total.append(y)

print(total)    