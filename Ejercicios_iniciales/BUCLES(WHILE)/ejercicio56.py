#Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.

print('''MENÚ
1. Bocadillo de calamares- 9 €"
2. Bocadillo de chistorra - 4.5 €
3. Bikini de jamón - 2.5 €"
ACOMPAÑAMIENTO
1. Patatas finas - 1.5 €
2. Patatas gruesas - 1.75 €
3. Patatas rústicas - 2 €
BEBIDAS
1. Coca cola - 2 €"
2. Acuarius - 1.5 €
3. Agua - 1 €"
''')
x=True
precio_total=0
total_pedidos=0
while x:
    total_descuento=0
    men=int(input("Número menú principal: "))
    acom=int(input("Número acompañamiento: "))
    bebida=int(input("Número bebida: "))
    if men ==1:
        precio_total+=9
    elif men==2:
        precio_total+=4.5
    elif men==3:
        precio_total+=2.5
    if acom ==1:
        precio_total+=1.5
    elif acom==2:
        precio_total+=1.75
    elif acom==3:
        precio_total+=2
    if bebida ==1:
        precio_total+=2
    elif bebida==2:
        precio_total+=1.5
    elif bebida==3:
        precio_total+=1
    total_pedidos+=1
    if input("Desea realizar otro pedido?(s/n): ")=="n":
        x=False
precio_iva=precio_total*1.1
if precio_iva > 30:
    precio_descuento=precio_iva*0.85
    total_descuento="15%"
elif precio_iva> 20:
    total_descuento="5%"
    precio_descuento=precio_iva*0.95
print(f'''RESUMEN
Número de pedidos: {total_pedidos}
Total a pagar: {precio_total}
Total con IVA: {precio_iva}
Total con un descuento del {total_descuento}: {round(precio_descuento, 2)}''')