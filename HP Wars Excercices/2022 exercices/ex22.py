year=input()
perma=year
day=13
counter=1
while True:
    month=counter
    year=perma
    if month==1 or month==2:
        month+=12
        year=int(year)
        year-=1
        year=str(year)
    c=year[:2]
    k=year[2:]
    res=(int(str((2.6*month-5.39))[0])+(int(str(int(k)/4)[0]))+(int(str(int(c)/4)[0]))+day+int(k)-2*int(c))%7
    print(res)
    if res==2:
        print(f"Martes y Trece will occur on 13/{counter}/{year}")
    counter+=1
    if counter==13:
        break

