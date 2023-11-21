class Map():
    def __init__(self):
        pass
    
    #*=blank b=boat hb=hit_boat
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
def setboats(a,b,c,d,e,f,g,h,i,j):
    list(a,b,c,d,e,f,g,h,i,j)
    print("If you place the boat verticaly, you must place the higher point")
    
    corr=False
    x=str()
    while x.isnumeric()==False and corr:
        x=input("In what vertical row do you want to place your boat (1-10): ")
        if x.isnumeric():
            if x>=1 and x<=10:
                corr=True
    x=int(x)-1
    a.pop(x)
    a.insert(x,"b")
    return a




p_map=Map()
c_map=Map()
print(p_map.a)
xd=setboats(a=p_map.a,b=p_map.b,c=p_map.c,d=p_map.d,e=p_map.e,f=p_map.f,g=p_map.g,h=p_map.h,i=p_map.i,j=p_map.j)
print(xd)
print(p_map.a)
