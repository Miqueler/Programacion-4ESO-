from random import choice
def añade_verbos():
    file=open("AHORCADO\diccionario.txt","a")
    final=input("Introduce la palabra que quieres añadir: ").lower()
    file.write(f"\n{final}")
    file.close()


x="s"
add=input("Quieres añadir alguna palabra al diccionario?(s/n): ")
if add == "s":
    añade_verbos()


with open("AHORCADO\diccionario.txt","r") as d:
    lista_palabrasecreta=d.readlines()
while x.lower()=="s":
    palabrasecreta=choice(lista_palabrasecreta)
    lista_partida=[]
    lista_ahorcado=[]
    c=0
    ahor=["A","H","O","R","C","A","D","O"]
    for i in range(len(palabrasecreta)):
        lista_partida.append("_")
    guess=""
    while lista_ahorcado!=["A","H","O","R","C","A","D","O"] and lista_partida!=list(palabrasecreta):
        letra=input("Introduce la letra que adivinas: ")
        if letra in list(palabrasecreta):
            indices=[i for i, x in enumerate(list(palabrasecreta)) if x == letra]
            for i in indices:
                lista_partida.pop(i)
                lista_partida.insert(i,letra)
                print(lista_partida)
        else:
            lista_ahorcado.append(ahor[c]); c+=1
            print(lista_partida)
            print(lista_ahorcado)
    if lista_ahorcado==["A","H","O","R","C","A","D","O"]:
        print(f"Has perdido, la palabra era {palabrasecreta}")
    else:
        print("Enhorabuena, has ganado")
    x=input("Quieres volver a jugar? (s/n): ")