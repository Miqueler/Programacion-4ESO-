# A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repe=[]
n_repe=[]

for i in lista1:
    if i in lista2:
        repe.append(i)
    else:
        n_repe.append(i)

for i in lista2:
    if i not in lista1 and i not in n_repe:
        n_repe.append(i)
print(f"Estan repetidas: {repe}")
print(f"No estan repetidas: {n_repe}")