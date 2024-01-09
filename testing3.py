jugar="s"

while jugar == "s":
    x=2
    while x>0:
        print("k")
        x-=1
    jugar=""
    while jugar != 's' and jugar!="n":
        jugar=input("Do you ....: (S/N): ").lower()
print("Se fini")