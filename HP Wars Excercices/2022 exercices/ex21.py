message=input()
test=bool()
for i in range(len(message)):
    if message[i]=="#" and message[i+1]=="#" and message[i+2]=="#":
        previous=int()
        following=int()
        try:
            previous=message[i-1]
            following=message[i+3]
        except IndexError:
            test=False
        try:
            previous=int(previous)
            following=int(following)
            total=previous+following
            if total==10:
                print("True")
                test=True
                break
            else:
                test=False
                break
        except ValueError:
            test=False
            

if test!=True:
    print("False")

