# Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra

wrd=input("Introduce la palabra secreta: ")
wrd_len=len(wrd)
guess=""
for i in range(wrd_len):
    guess=input("Introduce una letra: ")
    if guess in wrd:
        print("la letra existe")
    else:
        print("la letra no exisite")