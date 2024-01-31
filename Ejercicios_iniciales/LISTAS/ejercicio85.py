#Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
ing=[]
cast=[]
cat=[]
test=""
while test!="n":
    input("Introduce estudiante: ")
    ing.append(float(input("Nota Inglés: ")))
    cast.append(float(input("Nota Castellano: ")))
    cat.append(float(input("Nota Catalán: ")))
    test=input("Deseas introducir otro alumno s/n: ")
print(f"La mediana de catalán es: {sum(cat)/len(cat)}")
print(f"La mediana de castellano es: {sum(cast)/len(cast)}")
print(f"La mediana de inglés es: {sum(ing)/len(ing)}")