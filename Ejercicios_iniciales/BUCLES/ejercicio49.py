# A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

wrd=input("Introduce la palabra secreta: ")
wrd_len=len(wrd)
guess=""
for i in range(wrd_len):
    guess=input("Introduce una letra: ")
    if guess in wrd:
        print("la letra existe")
        cont=1
        for i in wrd:
            if guess == i:
                print(f"la letra se encuentra en la posición {cont}")
            cont+=1
    else:
        print("la letra no exisite")