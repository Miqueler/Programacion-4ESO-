
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
    boat_pos=[]

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
    
    direction=""
    while direction not in ["up","down","left","right"]:
            direction=input("In what direction do you want to place the boat (up, down, right, left): ")
    boat_pos.append(row)
    boat_pos.append(index)
    boat_pos.append(direction)
    return boat_pos

def place_boat(boat_lenght,a,b,c,d,e,f,g,h,i,j):
    boat_pos=get_boat_pos()
    if boat_pos[2]=="right":
            pass
print(get_boat_pos())
