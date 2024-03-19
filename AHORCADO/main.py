from random import choice
lista_palabrasecreta=["amigo","comer","jugar","correr","pitar","leer","ganar","esperar","casa","sol"]
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