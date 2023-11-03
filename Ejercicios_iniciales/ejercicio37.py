#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido
x=int(input("Cuantas notas quieres introducir?: "))
for i in range(x):
    nota=int(input("Introduce la nota: "))
    if nota<5:
        print("Asignatura suspendida")
    else:
        print("Asignatura aprobada")