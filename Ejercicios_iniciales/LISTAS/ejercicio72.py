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
        y=input("Introduce una letra: ")

        if y in acentos and y not in vocales:
            temp=acentos[y]
            if temp not in total:
                if y not in total and y.isnumeric()==False:
                    test=False
        elif y not in total and y.isnumeric()==False:
            if y in vocales:
                for i in total:
                    if i in acentos:
                        temp=acentos[i]
                        if temp==y:
                            test=True
                            break
                        else:
                            test=False
            else:
                test=False
    
    total.append(y)
print(total)    