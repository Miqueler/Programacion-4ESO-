#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=int(input("Introduce el lado: "))
men=int(input("Introduce la base menor: "))
may=int(input("Introduce la base mayor: "))
hight=int(input("Introduce la altura: "))
per=lado*2+men+may
area=((men+may)*hight)/2
print(f"El perímetro es: {per}")
print(f"El área es: {area}")