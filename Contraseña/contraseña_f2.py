run=True
while run:
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    print('''Instruccions:
        1.La contrasenya ha de tindre 8 caracters
        2.Ha de tindre les següents condicions:
            Un número entre 1 i 5 inclosos
            Una lletra minúscula
            Una lletra majúscula
            Un dels següents simbols *,_,@
            Una lletra minúscula
            Un número entre 6 i 9 inclosos
            Un dels següents símbols &,/,#
            Un número menor o igual a 5''')
    password=input("Introduce la contraseña: ")
    if len(password)==8:
        for i in password:
            #Comprovacions de nums
            if i.isnumeric():
                u=int(i)
                if u >= 1 and u<=5:
                    print(1)
                    c1+=1
                elif u>=6 and u<=9:
                    print(5)
                    c5+=1
                elif u<=5:
                    print(7)
                    c7+=1
            if i.isalpha():
                if i.islower():
                    print(2)
                    c2+=1
                elif i.isupper():
                    print(3)
                    c3+=1
            elif i in ["*","_","@"]:
                print(4)
                c4+=1
            
            elif i in ["&","/","#"]:
                print(6)
                c6+=1

    else:
        print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
    y=input("Si no quieres introducir otra contraseña introduce n: ")
    if y=="n":
        run=False