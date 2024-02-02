while True:
    dni=input("Introduce el DNI: ")
    if dni.isnumeric() and len(dni)==8:
        dni=int(dni)
        break
print("k")