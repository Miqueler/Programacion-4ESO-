#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
ing=[]
cast=[]
cat=[]
test=""
count=0
while test!="n":
    input("Introduce estudiante: ")
    ing.append(float(input("Nota Inglés: ")))
    cast.append(float(input("Nota Castellano: ")))
    cat.append(float(input("Nota Catalán: ")))
    test=input("Deseas introducir otro alumno s/n: ")
    count+=1
print(f"La media de catalán es: {round(sum(cat)/len(cat),2)}")
print(f"La media de castellano es: {round(sum(cast)/len(cast),2)}")
print(f"La media de inglés es: {round(sum(ing)/len(ing),2)}")
if count%2==0:
    print(f"La mediana de catalán es: {cat[int(count/2)]}")
    print(f"La mediana de castellano es: {int(cast[count/2])}")
    print(f"La mediana de inglés es: {int(ing[count/2])}")
else:
    count-=1
    print(f"La mediana de catalán es: {(cat[int(count/2)]+cat[int(1+(count/2))])/2}")
    print(f"La mediana de castellano es: {(cast[int(count/2)]+cast[int(1+(count/2))])/2}")
    print(f"La mediana de inglés es: {(ing[int(count/2)]+ing[int(1+(count/2))])/2}")