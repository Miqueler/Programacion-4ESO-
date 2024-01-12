# Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repe=[]
n_repe=[]

for i in lista1:
    if i in lista2:
        repe.append(i)
    else:
        n_repe.append(i)
print(f"Estan repetidas: {repe}")
print(f"No estan repetidas: {n_repe}")