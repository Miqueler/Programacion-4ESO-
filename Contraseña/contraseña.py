password=input("Introduce la contraseña: ")
if len(password)>=6 and len(password) <=8:
    #Pas 1
    try:
        if int(password[0])>5 or int(password[0]) <1:
            print("Error, el numero ha d'estar entre 1 i 5")
        else:
            print("Pas 1 completat")
    except ValueError:
        print("El primer caracter ha de ser un numero")
    #Pas 2
    if password[1].islower():
        print("Pas 2 completat")
    else:
        print("El segon caracter ha de ser una lletra en miniuscules")
    #Pas 3
    if password[2].isupper():
        print("Pas 3 completat")
    else:
        print("El tercer caracter ha de ser una lletra en majuscules")
    #Pas 4
    if password[3]in ["_", "@", "*"]:
        print("Pas 4 completat")
    else:
        print("El quart caracter ha de ser un dels següents caracters: (_,@,*)")
    #Pas 5
    if password[4].islower:
        print("Pas 5 completat")
    else:
        print("El cinqué caracter ha de ser una lletra en minúscula")
    #Pas 6
    try:
        if int(password[5])>=6 and int(password[5]) <=9:
            print("Pas 6 completat")
        else:
            print("Error, el numero ha d'estar entre 6 i 9")
    except ValueError:
        print("El sisé caracter ha de ser un número")
    #Pas 7
    if len(password)>=7:
        if password[6]in ["&", "/", "#"]:
            print("Pas 7 completat")
        else:
            print("El quart caracter ha de ser un dels següents caracters: (&,/,#)")
    #Pas 8
    if len(password)>=8:
        try:
            if int(password[7]) <=5:
                print("Pas 8 completat")
            else:
                print("Error, el numero ha d'estar entre 6 i 9")
        except ValueError:
            print("El vuité caracter ha de ser un número")
else:
    print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")