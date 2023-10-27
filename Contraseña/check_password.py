list_passwords=["2Aa*a","2Aa*a8#8a","9aA*a8#3","41A*a8#3","4ba*a8#3","4bA%a8#3","4bA*T8#3","4bA*t4#3","4bA*t7*3","4bA*t7#6","8BA*t7#4","8BA*t7#9","1bB_a7/4","1bB_a7/","1bB_a7"]
for i in list_passwords:
    password=i
    correct=True
    errores=""

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
    print("----------------------------------------------------")