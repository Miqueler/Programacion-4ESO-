#. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

if x>y:
    print(f"The first ({x}) one is bigger")
elif x<y:
    print(f"The second one ({y}) is bigger")
else:
    print("They are equal")
