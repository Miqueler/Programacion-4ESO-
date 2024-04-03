from random import choice
import time

#añadir el registro de las partidas a un txt
def añade_verbos():
    file=open("AHORCADO\dic.txt","a")
    final=input("Introduce la palabra que quieres añadir: ").lower()
    file.write(f"\n{final}")
    file.close()
def elimina_verbos():
    fichero=open("AHORCADO\dic.txt")
    dictionary=fichero.readlines()
    user_verb=input("Introduce la palabra que quieres eliminar: ").lower()
    c=0
    linea=""
    while c<len(dictionary):
        if dictionary[c]==user_verb:
            linea=dictionary[c].split(";")
            break
        c+=1
    if linea=="":
        print("La palabra no está en el diccionario")
    else:
        print(f"El verbo que quieres eliminar es:")
        print(dictionary[c])
        if input("Estas seguro (s): ").lower()=="s":
            dictionary.pop(c)
            file=open("AHORCADO\dic.txt","w")
            file.writelines(dictionary)
            file.close()

x="s"
add=input("Quieres añadir alguna palabra al diccionario?(s/n): ")
if add == "s":
    añade_verbos()
delete=input("Quieres eliminar alguna palabra al diccionario?(s/n): ")
if delete=="s":
    elimina_verbos()

with open("AHORCADO\dic.txt","r") as d:
    lista_palabrasecreta=d.read().splitlines()

while x.lower()=="s":
    palabrasecreta=choice(lista_palabrasecreta)
    lista_partida=[]
    lista_ahorcado=[]
    lista_usadas=[]
    aciertos=[]
    errores=[]
    tem=time.time()
    c=0
    ahor=["A","H","O","R","C","A","D","O"]
    for i in range(len(palabrasecreta)):
        lista_partida.append("_")
    print(lista_partida)
    guess=""
    while lista_ahorcado!=["A","H","O","R","C","A","D","O"] and lista_partida!=list(palabrasecreta):
        local_test=True
        while local_test:
            letra=input("Introduce la letra que adivinas: ")
            if letra not in lista_usadas:
                local_test=False
            else:
                print("Ya has usado esta letra")
                print(lista_usadas)

        lista_usadas.append(letra)
        if letra in list(palabrasecreta):
            aciertos.append(letra)
            indices=[i for i, x in enumerate(list(palabrasecreta)) if x == letra]
            for i in indices:
                lista_partida.pop(i)
                lista_partida.insert(i,letra)
            print(lista_partida)
        else:
            lista_ahorcado.append(ahor[c]); c+=1
            print(lista_partida)
            print(lista_ahorcado)
            errores.append(letra)
        print(lista_usadas)
    if lista_ahorcado==["A","H","O","R","C","A","D","O"]:
        print(f"Has perdido, la palabra era {palabrasecreta}")
    else:
        print("Enhorabuena, has ganado")
    print(f"Has acertado {len(aciertos)} veces y has fallado {len(errores)} veces")
    print(f"Has tardado {round(time.time()-tem,1)} segundos")

    lista_palabrasecreta.pop(lista_palabrasecreta.index(palabrasecreta))
    file=open("AHORCADO\dic.txt","w")
    lista_palabrasecreta.sort()
    for i in range(len(lista_palabrasecreta)):
        file.write(f"{lista_palabrasecreta[i]}\n")
    file.close()

    x=input("Quieres volver a jugar? (s/n): ")