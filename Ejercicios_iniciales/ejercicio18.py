#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por
#teclado el número de menores y el número de adultos que asisten al cine.

adultos=int(input("Introduce el número de adultos: "))
menores=int(input("Introduce el número de menores: "))

precio_a=round(adultos*10.8, 1)
precio_b=menores*6

print(f"El precio total del cine para {menores} menor/es es: {precio_b}€")
print(f"El precio total del cine para {adultos} adulto/s es: {precio_a}€")