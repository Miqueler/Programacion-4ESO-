#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos
mark=int(input("Introduce la nota: "))
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