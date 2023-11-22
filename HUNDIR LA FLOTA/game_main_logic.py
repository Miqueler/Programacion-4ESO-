def get_boat_pos():
    boat_pos=""

    row=""
    all_letters_map=["a","b","c","d","e","f","g","h","i","j"]
    while row not in all_letters_map:
            row=input("In what row do you want to place your boat (a-j): ")
    row=all_letters_map.index(row)
    corr=False
    x=""
    while corr==False:
        x=input("In what vertical row do you want to place your boat (1-10): ")
        if x.isnumeric():
            index=int(x)-1
            if index>=0 and index<=9:
                corr=True

    boat_pos+=str(row)
    boat_pos+=str(index)
    #Returns the position given as an index: first the row and then the index in line
    return boat_pos

def get_boat_direction(boat_lenght,boat_pos):
    row=int(boat_pos[0])
    index=int(boat_pos[1])
    correct=False
    while not correct:
        direction=""
        while direction not in ["up", "down", "left", "right"]:
            direction=input("In what direction do you want to place the boat (up, down, right, left): ")
        if direction == "up":
            if row - boat_lenght>=0:
                correct=True
                direction=0
        elif direction == "down":
            if row + boat_lenght<=9:
                correct=True
                direction=1
        elif direction == "left":
            if index - boat_lenght>=0:
                correct=True
                direction=2
        elif direction == "right":
            if row + boat_lenght<=9:
                correct=True
                direction=3
        else:
            print("ERROR in direction")
    #Returs direction as a number up=0 down=1 left=2 right=3
    return direction

def place_boat(boat_lenght,boat_pos,direciton):
    current_boat_list=[boat_pos]
    for i in range(boat_lenght):
        counter=i+1
        iter_boat=boat_pos
        if direciton==0:
            iter_boat=int(boat_pos[0])-counter
            iter_boat=str(iter_boat)+boat_pos[1]
        elif direciton==1:
            iter_boat=int(boat_pos[0])+counter
            iter_boat=str(iter_boat)+boat_pos[1]
        elif direciton==2:
            iter_boat=int(boat_pos[1])-counter
            iter_boat=str(iter_boat)+boat_pos[0]
        elif direciton==3:
            iter_boat=int(boat_pos[1])+counter
            iter_boat=str(iter_boat)+boat_pos[0]
        current_boat_list.append(iter_boat)
    return current_boat_list