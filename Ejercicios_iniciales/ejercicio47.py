#. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

n1=int(input("Itroduce el primer número: "))
n2=int(input("Itroduce el primer segindo: "))
res=""
if n1>n2:
    while n1>=n2:
        res+=str(n1)+"-"
        n1-=1
elif n1<n2:
    while n2>=n1:
        res+=str(n1)+"-"
        n1+=1

print(res[:-1])

