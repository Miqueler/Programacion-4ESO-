l1=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
flag="s"
lon=int()
num=int()
lista_intentos=[]
dni_corr=[]
dni_incorr=[]
while flag=="s":
    dni=str()
    while not dni.isnumeric() or len(dni)!=8:   
        dni=input("Introduce el DNI: ")
        if dni.isnumeric()==False:
            print("el valor introducido debe ser numérico")
            lista_intentos.append(1)
            dni_incorr.append(dni)
            num+=1
        if len(dni)!=8:
            print("el valor introducido no cumple con la longitud correcta")
            lon+=1
            lista_intentos.append(0)
            dni_incorr.append(dni)
    lista_intentos.append(2)
    dni_corr.append(dni)
    resto=int(dni)%23

    letra=l1[resto]
    print(dni+"-"+letra)
    flag=input("Quieres seguir? (s/n): ").lower()
    while flag!="s" and flag !="n":
        flag=input("Quieres seguir? (s/n): ").lower()

print(sorted(dni_corr))
print(sorted(dni_incorr))
print(len(dni_incorr))
print(len(dni_corr))
print(f"El número de intentos es: {len(lista_intentos)} ")
print(f"El porcentaje de DNI's correctos es: {round(len(dni_corr)/len(lista_intentos)*100,1)}%")
print(f"El porcentaje de DNI's incorrectos es: {round(len(dni_incorr)/len(lista_intentos)*100,1)}%")
print(f"El porcentaje de DNI's con error de longitud es: {round(lon/len(lista_intentos)*100,1)}%")
print(f"El porcentaje de DNI's con error de longitud es: {round(num/len(lista_intentos)*100,1)}%")
print("Final del programa")