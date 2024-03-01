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
    return [verbos,formas]

def funcion_menu():
    decision=input('''Que quieres hacer?:
1: Jugar a conjugar verbos
2: Traducir del español al inglés
3: Traducir del inglés al español
4: Jugar a "desorden total"
5: Consultar el diccionario
6: Añadir nuevos verbos al txt
7: Eliminar verbos del txt
8: Salir''').lower()
res=conjugar_verbos()
control_errores(res[0],res[1])