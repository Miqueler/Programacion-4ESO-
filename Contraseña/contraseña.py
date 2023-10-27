correct=True
errores=""
print('''Instruccions:
        1.La contrasenya ha de tindre entre 6 i 8 caracters
        2.Forçar els següents valors en les següents posicions:
            Posició 1 Un número entre 1 i 5 inclosos
            Posició 2 Una lletra minúscula
            Posició 3 Una lletra majúscula
            Posició 4 Un dels següents simbols *,_,@
            Posició 5 Una lletra minúscula
            Posició 6 Un número entre 6 i 9 inclosos
            Posició 7 Un dels següents símbols &,/,#
            Posició 8 Un número menor o igual a 5''')
password=input("Introduce la contraseña: ")
if len(password)>=6 and len(password) <=8:
    #Pas 1
    try:
        if int(password[0])>5 or int(password[0]) <1:
            errores+="Error en el caracter 1 "
            correct=False
        
    except ValueError:
        errores+="Error en el caracter 1 "
        correct=False
    #Pas 2
    if not password[1].islower():
        errores+="Error en el caracter 2 "
        correct=False
    #Pas 3
    if not password[2].isupper():
        errores+="Error en el caracter 3 "
        correct=False
    #Pas 4
    if not password[3]in ["_", "@", "*"]:
        errores+="Error en el caracter 4 "
        correct=False
    #Pas 5
    if not password[4].islower():
        errores+="Error en el caracter 5 "
        correct=False
    #Pas 6
    try:
        if not int(password[5])>=6 and int(password[5]) <=9:
            errores+="Error en el caracter 6 "
            correct=False
    except ValueError:
        errores+="Error en el caracter 6 "
        correct=False
    #Pas 7
    if len(password)>=7:
        if not password[6]in ["&", "/", "#"]:
            errores+="Error en el caracter 7 "
            correct=False
    #Pas 8
    if len(password)>=8:
        try:
            if not int(password[7]) <=5:
                errores+="Error en el caracter 8 "
                correct=False
        except ValueError:
            errores+="Error en el caracter 8 "
            correct=False
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
    correct=False

if correct:
    print("La contraseña és correcta")
else:
    print(errores)