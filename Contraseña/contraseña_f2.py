run=True
while run:
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    print('''Instruccions:
        1.La contrasenya ha de tindre 8 caracters
        2.Ha de tindre les següents condicions:
            Un número entre 1 i 5 inclosos x2
            Una lletra minúscula x2
            Una lletra majúscula
            Un dels següents simbols *,_,@
            Un número entre 6 i 9 inclosos
            Un dels següents símbols &,/,#''')
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
            if i.isalpha():
                if i.islower():
                    c2+=1
                elif i.isupper():
                    c3+=1
            elif i in ["*","_","@"]:
                c4+=1
            elif i in ["&","/","#"]:
                c6+=1
        if c1!=2:
            print("Error 1")
        if c2!=2:
            print("Error 2")
        if c3!=1:
            print("Error 3")
        if c4!=1:
            print("Error 4")
        if c5!=1:
            print("Error 5")
        if c6!=1:
            print("Error 6")


    else:
        print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
    y=input("Si no quieres introducir otra contraseña introduce n: ")
    if y=="n":
        run=False