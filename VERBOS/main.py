from random import randint
with open("VERBOS\diccionario.txt") as d:
    dictionary=d.readlines()
def control_errores(verbos,formas):
    for i in range(len(verbos)):
        if formas[i][0]==0 and formas[i][1]==0:
            print(f"Repasa el pasado y el participio del verbo {verbos[i]}")
        elif formas[i][0]==0:
            print(f"Repasa el pasado del verbo {verbos[i]}")
        elif formas[i][1]==0:
            print(f"Repasa el participio del verbo {verbos[i]}")

def conjugar_verbos(dictionary):
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
            formas.append([1])
        else:
            print(f"Error, el pasado de {linea[0]} es {pasado[0]}")
            formas.append([0])
        user_participio=input("Intoduce el participio: ").lower()
        if user_participio in participio:
            print("Correcto")
            formas[cont].append(1)
        else:
            print(f"Error, el participio de {linea[0]} es {participio[0]}")
            formas[cont].append(0)
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
        cont+=1
    control_errores(verbos, formas)
def esp_a_ing(dictionary):
    while True:
        index=randint(0,191)
        linea= dictionary[index].split(";")
        esp=linea[3].split(",")
        eng=linea[0]
        user_eng=input(f"Traduce {esp[0]} al inglés")
        if user_eng in eng:
            print("Correcto")
        else: print(f"Error, una traducción es: {eng[0]}")
        if input("Si deseas participar introduce s: ").lower()!="s":
            break
def funcion_menu(dictionary):
    decision=input('''Que quieres hacer?:
1: Jugar a conjugar verbos
2: Traducir del español al inglés
3: Traducir del inglés al español
4: Jugar a "desorden total"
5: Consultar el diccionario
6: Añadir nuevos verbos al txt
7: Eliminar verbos del txt
8: Salir''')
    if decision=="1":
        conjugar_verbos(dictionary)
    elif decision=="2":
        esp_a_ing(dictionary)
funcion_menu(dictionary)