x=input().split()
if int(x[0])==int(x[2]) and int(x[1])==int(x[3]):
    print("=")
elif int(x[0])>=int(x[2]) and int(x[1])<=int(x[3]):
    print("1")
elif int(x[0])<=int(x[2]) and int(x[1])>=int(x[3]):
    print("2")
else: print("?")