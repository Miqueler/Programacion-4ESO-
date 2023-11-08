#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
voc=""
con=""
error=0
x=input("Introduce tu palabra: ")
for i in range(len(x)):
    if x[i] in 'aeiouàèìòùáéíóú':
        voc+=x[i]
    elif x[i] in 'bcdfghjklmnñpqrstvwxyz':
        con+=x[i]
    else:
        con+=x[i]
        error+=1
if error!=0:
    con+=" ¿?"

print(f"Las vocales de la palabra Abrigo son: {voc}")
print(f"Las consonantes de la palabra Abrigo son: {con}")