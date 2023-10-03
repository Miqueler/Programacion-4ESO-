#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
mark=float(input("Introduce la nota: "))
if mark>=0 and mark<=10:
    if mark<5:
        print("Has suspendido")
    elif mark>=8.5: 
        print("Has sacado un excelente")
    elif mark<8.5 and mark>=6.5: 
        print("Has sacado un notable")
    elif mark<6.5 and mark>=5: 
        print("Has sacado un suficiente")

else:
    print("La nota ha de ser entre 0 y 10")