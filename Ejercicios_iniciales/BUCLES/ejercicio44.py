#Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
x=0
y=""
while x<100:
    y+=str(x)+","
    x+=3
print(y[:-1])
