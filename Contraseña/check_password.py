list_passwords=["2Aa*a","2Aa*a8#8a","9aA*a8#3","41A*a8#3","4ba*a8#3","4bA%a8#3","4bA*T8#3","4bA*t4#3","4bA*t7*3","4bA*t7#6","8BA*t7#4","8BA*t7#9","1bB_a7/4","1bB_a7/","1bB_a7"]
for i in list_passwords:
    password=i
    correct=True
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
        if not password[4].islower():
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
    print("----------------------------------------------------")