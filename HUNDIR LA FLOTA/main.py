
a=["*","*","*","*","*","*","*","*","*","*"]
b=["*","*","*","*","*","*","*","*","*","*"]
c=["*","*","*","*","*","*","*","*","*","*"]
d=["*","*","*","*","*","*","*","*","*","*"]
e=["*","*","*","*","*","*","*","*","*","*"]
f=["*","*","*","*","*","*","*","*","*","*"]
g=["*","*","*","*","*","*","*","*","*","*"]
h=["*","*","*","*","*","*","*","*","*","*"]
i=["*","*","*","*","*","*","*","*","*","*"]
j=["*","*","*","*","*","*","*","*","*","*"]
#1*5, 1*4, 2*3, 1*2
def get_boat_pos():
    boat_pos=""

    row=""
    while row not in ["a","b","c","d","e","f","g","h","i","j"]:
            row=input("In what row do you want to place your boat (a-j): ")

    corr=False
    x=""
    while corr==False:
        x=input("In what vertical row do you want to place your boat (1-10): ")
        if x.isnumeric():
            index=int(x)-1
            if index>=0 and index<=9:
                corr=True

    boat_pos+=row
    boat_pos+=str(index)
    return boat_pos

def place_boat(boat_lenght):
    if boat_lenght.
print(get_boat_pos())
