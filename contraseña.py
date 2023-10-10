x=input("Introduce la contraseña: ")
if len(x)>=6 and len(x) <=8:
    #Pas 1
    try:
        if int(x[0])>5 or int(x[0]) <1:
            print("Error, el numero ha d'estar entre 1 i 5")
        else:
            print("Pas 1 completat")
    except ValueError:
        print("El primer caracter ha de ser un numero")
    #Pas 2
    if x[1].islower():
        print("Pas 2 completat")
    else:
        print("El segon caracter ha de ser una lletra en miniuscules")
    #Pas 3
    if x[2].isupper():
        print("Pas 3 completat")
    else:
        print("El tercer caracter ha de ser una lletra en majuscules")
    #Pas 4
    if x[3]in ["_", "@", "*"]:
        print("Pas 4 completat")
    else:
        print("El quart caracter ha de ser un dels següents caracters: (_,@,*)")
    #Pas 5
    if x[4].islower:
        print("Pas 5 completat")
    else:
        print("El cinqué caracter ha de ser una lletra en minúscula")
    #Pas 6
    try:
        if int(x[5])>=6 and int(x[5]) <=9:
            print("Pas 6 completat")
        else:
            print("Error, el numero ha d'estar entre 6 i 9")
    except ValueError:
        print("El sisé caracter ha de ser un número")
    #Pas 7
    if len(x)>=7:
        if x[6]in ["&", "/", "#"]:
            print("Pas 7 completat")
        else:
            print("El quart caracter ha de ser un dels següents caracters: (&,/,#)")
    #Pas 8
    if len(x)>=8:
        try:
            if int(x[7]) <=5:
                print("Pas 8 completat")
            else:
                print("Error, el numero ha d'estar entre 6 i 9")
        except ValueError:
            print("El vuité caracter ha de ser un número")
else:
    print(f"Error, el password té una longitud de {len(x)} caràcters i no compleix els requisits")