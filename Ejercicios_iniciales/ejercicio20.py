#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if x<=10 and x>=0:
    if y<=10 and y>=0:
        if x>y:
            print(f"The first ({x}) one is bigger")
        elif x<y:
            print(f"The second one ({y}) is bigger")
        else:
            print("They are equal")
    else:
        print("The number must be between 0 and 10")
else:
    print("The number must be between 0 and 10")
    