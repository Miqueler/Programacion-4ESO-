run=True
while run:
    print('''Instruccions:
        1.La contrasenya ha de tindre entre 6 i 8 caracters
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
    if len(password)>=6 and len(password) <=8:
        for i in password:
            if i >= 1 and i<=5:
                print(1)
            elif i.islower():
                print(2)
            elif i.isupper():
                print(3)
            elif i in ["*","_","@"]:
                print(4)
            elif i>=6 and i<=9:
                print(5)
            elif i in ["&","/","#"]:
                print(6)
            elif i<=5:
                print(7)

    else:
        print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
    y=input("Si no quieres introducir otra contraseña introduce n: ")
    if y=="n":
        run=False