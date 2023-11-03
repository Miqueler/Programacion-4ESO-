#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
voc=""
con=""
x=input("Introduce tu palabra: ")
for i in range(len(x)):
    if x[i].