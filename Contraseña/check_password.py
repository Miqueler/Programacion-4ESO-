list_passwords=["2Aa*a","2Aa*a8#8a","9aA*a8#3","41A*a8#3","4ba*a8#3","4bA%a8#3","4bA*T8#3","4bA*t4#3","4bA*t7*3","4bA*t7#6","8BA*t7#4","8BA*t7#9","1bB_a7/4","1bB_a7/","1bB_a7"]
for i in list_passwords:
    password=i
    long=len(password)
    ok=0
    error=""
    if not long>=6 and long<=8:
        print(f"Error, el password té una longitud de {long} caràcters i no compleix els requisits")
    else:
        if int(password[0])>=1 and int(password[0])<=5: 
            ok+=1
        else:    
            error=error+"Error en el caracter 1"
        if password[1].islower():
            ok+=1
        else:
            error=error+"Error en el caracter 2"
        if password[2].isupper():
            ok+=1
        else:
            error=error+"Error en el caracter 3"
        if password[3] in ["*","_","€"]:
            ok+=1
        else:
            error=error+"Error en el caracter 3"
        if password[4].islower():
            ok+=1
        else:
            error=error+"Error en el caracter 4"
        if int(password[5])>=6 and int (password[5])<=9:
            ok+=1
        else:
            error=error+"Error en el caracter 5"
        if password[6] in ["&","/","#"]:
            ok+=1
        else:
            error=error+"Error en el caracter 6"
        if int(password[7])<=5:
            ok+=1
        else:
            error=error+"Error en el caracter 7"
    print(error)
    print("----------------------------------------------------")