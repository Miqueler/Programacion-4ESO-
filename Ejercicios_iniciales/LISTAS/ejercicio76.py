#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
num=[]
let=[]
for i in lista1:
    if i.isnumeric():
        num.append(int(i))
    else:
        let.append(i)
if input("Introduce 1 para visualizar en orden ascendente o 2 descendente: ")=="1":
    num.sort()
    let.sort(key=str.casefold)
else:
    num.sort(reverse=True)
    let.sort(reverse=True,key=str.casefold)
print(num)
print(let)