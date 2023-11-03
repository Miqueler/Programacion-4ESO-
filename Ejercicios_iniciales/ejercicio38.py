#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

x=int(input("Cuantas notas quieres introducir?: "))
for i in range(x):
    nota=int(input("Introduce la nota: "))
    if nota >=0 and nota <=10:
        if nota<5:
            print("Asignatura suspendida")
        else:
            print("Asignatura aprobada")
    else:
        print("Has introducido una nota equivocada")