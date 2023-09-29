#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if 0>=x<=10 or 0>=y<=10:
    if x>y:
        print(f"The first ({x}) one is bigger")
    elif x<y:
        print(f"The second one ({y}) is bigger")
    else:
        print("They are equal")
else:
    print("The number must be between 0 and 10")
    