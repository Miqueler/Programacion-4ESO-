x=True
while x:
    try:
        dni=int(input("Introduce el número del DNI: "))
        x=False
        if x>9999999 and x<100000000:
            print("Tdo bien")
        elif x<9999999 or x>100000000:
            x=True 
            print("Ha de ser un número de 8 dígitos")
    except ValueError:
        print("Ha de ser un número de 8 dígitos")
        x=True
    