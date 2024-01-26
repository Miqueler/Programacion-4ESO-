#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
may=0
let=0
num=0
total=0
for i in lista1:
    if i.isnumeric():
        num+=1
        total+=int(i)
    elif i.isalpha():
        let+=1
        if i.isupper():
            may+=1


print(f"Número de valores: {len(lista1)}")
print(f"Cantidad de números: {num}")
print(f"Cantidad de letras: {let}")
print(f"Cantidad de mayúsculas: {may}")
print(f"Suma total de números: {total}")