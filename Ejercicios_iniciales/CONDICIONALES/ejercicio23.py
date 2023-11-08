#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

mark=float(input("Introduce la nota: "))
if mark>=0:
    if mark<=10:
        if mark<5:
            print("Has sacado un insuficiente")
        elif mark>=8.5: 
            print("Has sacado un excelente")
        elif mark>=6.5:
            print("Has sacado un notable")
        else:
            print("Has sacado un suficiente")
    else:
        print("La nota ha de esta entre 10 y 0")
else:
    print("La nota ha de esta entre 10 y 0")