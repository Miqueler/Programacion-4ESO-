#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
secs= int(input("Di el nombre de segundos: "))
mins=secs/60
hours=round(mins/60,2)
print(f"el número de minutos es: {mins} y en horas es: {hours}")