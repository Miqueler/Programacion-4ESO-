#Crea un programa que cuente todos los números pares hasta el número 50
par=0
i_par=0
for i in range(1,51):
    if i%2==0:
        par+=1
    else:
        i_par+=1
print(f"El total de pares es: {i_par}")
print(f"El total de impares es: {i_par}")