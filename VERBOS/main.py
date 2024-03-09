from random import randint,choice
with open("VERBOS/diccionario.txt") as d:
    dictionary=d.readlines()

def control_errores(verbos,formas):
    for i in range(len(verbos)):
        if formas[i][0]==0 and formas[i][1]==0:
            print(f"Repasa el pasado y el participio del verbo {verbos[i]}")
        elif formas[i][0]==0:
            print(f"Repasa el pasado del verbo {verbos[i]}")
        elif formas[i][1]==0:
            print(f"Repasa el participio del verbo {verbos[i]}")

def conjugar_verbos(dictionary,punt):
    cont=0
    verbos=[]
    formas=[]
    while True:
        index=randint(0,191)
        linea= dictionary[index].split(";")
        pasado=linea[1].split(",")
        participio=linea[2].split(",")
        print(f"El verbo es: {linea[0]}")
        verbos.append(linea[0])
        user_pasado=input("Intoduce el pasado: ").lower()
        if user_pasado in pasado:
            print("Correcto")
            punt+=1
            formas.append([1])
        else:
            print(f"Error, el pasado de {linea[0]} es {pasado[0]}")
            formas.append([0])
        user_participio=input("Intoduce el participio: ").lower()
        if user_participio in participio:
            print("Correcto")
            punt+=1
            formas[cont].append(1)
        else:
            print(f"Error, el participio de {linea[0]} es {participio[0]}")
            formas[cont].append(0)
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
        cont+=1
    control_errores(verbos, formas)
    return punt
def esp_a_ing(dictionary,punt):
    while True:
        index=randint(0,191)
        linea= dictionary[index].split(";")
        esp=linea[3].split(",")
        eng=linea[0]
        user_eng=input(f"Traduce {esp[0]} al inglés: ")
        if user_eng in eng:
            print("Correcto")
            punt+=1
        else: print(f"Error, una traducción es: {eng[0]}")
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
    return punt

def ing_a_esp(dictionary,punt):
    while True:
        index=randint(0,191)
        linea= dictionary[index].split(";")
        esp=linea[3].split(",")
        eng=linea[0]
        user_esp=input(f"Traduce {eng[0]} al español: ")
        if user_esp in esp:
            print("Correcto")
            punt+=1
        else: print(f"Error, una traducción es: {esp[0]}")
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
    return punt

def desorden_total(dictionary,punt):
    while True:
        index=randint(0,191)
        linea= dictionary[index].split(";")
        st_verbo=linea[0]
        verbo=list(linea[0])
        r_verbo=""
        for i in range(len(verbo)):
            r_c=choice(verbo)
            verbo.pop(verbo.index(r_c))
            r_verbo=r_verbo+r_c
        if input(f"Ordena el verbo: {r_verbo}: ") == st_verbo:
            print("Correcto")
            punt+=1
        else:
            print(f"Error, el verbo es: {st_verbo}")
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
    return punt
def consulta(dictionary):
    user_verb=input("Introduce el verbo en infinitivo que quieres consultar: ")
    c=0
    linea=""
    while c<len(dictionary):
        if dictionary[c].split(";")[0]==user_verb:
            linea=dictionary[c].split(";")
            break
        c+=1
    if linea=="":
        print("El verbo no está en el diccionario")
    else:
        print(f"El pasado es: {linea[1]}")
        print(f"El participio es: {linea[2]}")
        print(f"La traducción es: {linea[3]}")
def añade_verbos():
    file=open("VERBOS/diccionario.txt","a")
    ing=input("Introduce el verbo en infinitivo (inglés) que quieres añadir: ").lower()
    pasado=input("Introduce el pado del verbo que quieres añadir: ").lower()
    participio=input("Introduce el participio del verbo que quieres añadir: ").lower()
    esp=input("Inttoduce la traducción al español del verbo: ").lower()
    final=f"{ing};{pasado};{participio};{esp}"
    file.write(f"\n{final}")
def elimina_verbos(dictionary):
    user_verb=input("Introduce el verbo en infinitivo que quieres eliminar: ").lower()
    c=0
    linea=""
    while c<len(dictionary):
        if dictionary[c].split(";")[0]==user_verb:
            linea=dictionary[c].split(";")
            break
        c+=1
    if linea=="":
        print("El verbo no está en el diccionario")
    else:
        print(f"El verbo que quieres eliminar es:")
        print(dictionary[c])
        if input("Estas seguro (s): ").lower()=="s":
            dictionary.pop(c)
            file=open("VERBOS/diccionario.txt","w")
            file.writelines(dictionary)
def funcion_menu(dictionary,points):
    decision=input('''Que quieres hacer?:
1: Jugar a conjugar verbos
2: Traducir del español al inglés
3: Traducir del inglés al español
4: Jugar a "desorden total"
5: Consultar el diccionario
6: Añadir nuevos verbos al txt
7: Eliminar verbos del txt
8: Salir
''')
    if decision=="1":
        points=conjugar_verbos(dictionary,points)
    elif decision=="2":
        points=esp_a_ing(dictionary,points)
    elif decision=="3":
        points=ing_a_esp(dictionary,points)
    elif decision=="4":
        points=desorden_total(dictionary,points)
    elif decision=="5":
        consulta(dictionary)
    elif decision=="6":
        añade_verbos()
    elif decision=="7":
        elimina_verbos(dictionary)
points=0
test=True
while test:
    points=funcion_menu(dictionary,points)
    if input("¿Quieres continuar?(s/n): ").lower()=="n":
        test=False