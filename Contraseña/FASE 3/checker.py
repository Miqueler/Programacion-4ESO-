def check(password):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    correct=True
    if len(password)==8:
        for i in password:
            #Comprovacions de nums
            if i.isnumeric():
                u=int(i)
                if u >= 1 and u<=5:
                    c1+=1 
                elif u>=6 and u<=9:
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
            correct=False
        if c2!=2:
        #    print("Error 2")
            correct=False
        if c3!=1:
        #    print("Error 3")
            correct=False
        if c4!=1:
        #   print("Error 4")
            correct=False
        if c5!=1:
        #   print("Error 5")
            correct=False
        if c6!=1:
        #    print("Error 6")
            correct=False
        if correct:
        #    print("Todo bien, la contraseña es correcta!")
            is_correct=2
        else:
            print("La contraseña tiene errores!")
            is_correct=1
    else:
        print(f"Error, el password té una longitud de {len(password)} caràcters i no compleix els requisits")
        is_correct=0
    
    return is_correct
