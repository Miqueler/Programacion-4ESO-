#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
mark=float(input("Enter the mark: "))
if mark>=0 and mark<=10:
    if mark<5:
        print("You failed")
    else: 
        print("You passed")
else:
    print("The mark must be between 0 and 10")