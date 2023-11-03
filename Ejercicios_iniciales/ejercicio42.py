#Imprima el siguiente patrón con el ciclo for
x=""
for i in range(5):
    x+="*"
    print(x)
for i in range(4):
    x=x[1:]
    print(x)