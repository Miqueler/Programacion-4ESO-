correct=True

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
            print("El primer caracter ha d'estar entre 1 i 5")
            correct=False
        
    except ValueError:
        print("El primer caracter ha de ser un número")
        correct=False
    #Pas 2
    if not password[1].islower():
        print("El segon caracter ha de ser una lletra en miniuscules")
        correct=False
    #Pas 3
    if not password[2].isupper():
        print("El tercer caracter ha de ser una lletra en majuscules")
        correct=False
    #Pas 4
    if not password[3]in ["_", "@", "*"]:
        print("El quart caracter ha de ser un dels següents caracters: (_,@,*)")
        correct=False
    #Pas 5
    if not password[4].islower:
        print("El cinqué caracter ha de ser una lletra en minúscula")
        correct=False
    #Pas 6
    try:
        if not int(password[5])>=6 and int(password[5]) <=9:
            print("Sisé caracter ha de ser un numero entre 6 i 9")
            correct=False
    except ValueError:
        print("El sisé caracter ha de ser un número")
        correct=False
    #Pas 7
    if len(password)>=7:
        if not password[6]in ["&", "/", "#"]:
            print("El seté caracter ha de ser un dels següents caracters: (&,/,#)")
            correct=False
    #Pas 8
    if len(password)>=8:
        try:
            if not int(password[7]) <=5:
                print("El vuité caracter ha de ser un número entre 6 i 9")
                correct=False
        except ValueError:
            print("El vuité caracter ha de ser un número")
            correct=False
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
    correct=False

if correct:
    print("La contraseña és correcta")