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

def check_all_directions(boat_lenght,boat_pos,all_boats_list):
    row=int(boat_pos[0])
    index=int(boat_pos[1])
    up_possible=True
    down_possible=True
    left_possible=True
    right_possible=True
    #Check for up
    if row - boat_lenght>=0:
        full_boat_list=[]
        for i in range(boat_lenght-1):
            counter=i+1
            iter_boat=boat_pos
            iter_boat=int(boat_pos[0])-counter
            iter_boat=str(iter_boat)+boat_pos[1]
            full_boat_list.append(iter_boat)
        for i in all_boats_list:
            for x in full_boat_list:
                if x in i:
                    up_possible=False
                    break
    else:
        up_possible=False
    #Check for down
    if row + boat_lenght<=9:
        full_boat_list=[]
        for i in range(boat_lenght-1):
            counter=i+1
            iter_boat=boat_pos
            iter_boat=int(boat_pos[0])+counter
            iter_boat=str(iter_boat)+boat_pos[1]
            full_boat_list.append(iter_boat)
        for i in all_boats_list:
            for x in full_boat_list:
                if x in i:
                    down_possible=False
                    break
    else:
        down_possible=False
    #Check for left
    if index - boat_lenght>=0:
        full_boat_list=[]
        for i in range(boat_lenght-1):
            counter=i+1
            iter_boat=boat_pos
            iter_boat=int(boat_pos[1])-counter
            iter_boat=boat_pos[0]+str(iter_boat)
            full_boat_list.append(iter_boat)
        for i in all_boats_list:
            for x in full_boat_list:
                if x in i:
                    left_possible=False
                    break
    else:
        left_possible=False
    #Check for right
    if index + boat_lenght<=9:
        full_boat_list=[]
        for i in range(boat_lenght-1):
            counter=i+1
            iter_boat=boat_pos
            iter_boat=counter+int(boat_pos[1])
            iter_boat=boat_pos[0]+str(iter_boat)
            full_boat_list.append(iter_boat)
        for i in all_boats_list:
            for x in full_boat_list:
                if x in i:
                    right_possible=False
                    break
    else:
        right_possible=False
    if up_possible==False and down_possible==False and left_possible==False and right_possible==False:
        return False
    else:
        return True

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
            if index + boat_lenght<=9:
                correct=True
                direction=3
        else:
            print("ERROR in direction")
    #Returs direction as a number up=0 down=1 left=2 right=3
    return direction

def place_boat(boat_lenght,boat_pos,direciton):
    current_boat_list=[boat_pos]
    for i in range(boat_lenght-1):
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
            iter_boat=boat_pos[0]+str(iter_boat)
        elif direciton==3:
            iter_boat=int(boat_pos[1])+counter
            iter_boat=boat_pos[0]+str(iter_boat)
        current_boat_list.append(iter_boat)
    return current_boat_list

def check_if_placement_possible(all_boats_list,boat_lenght):
    can_place_boat_check_2=False
    impossible_placement_check=False
    while not impossible_placement_check:
        can_place_boat_check_1=False
        while not can_place_boat_check_1:
            boat_pos=get_boat_pos()    
            for i in all_boats_list:
                if boat_pos in i:
                    can_place_boat_check_1=False
                    break
                else:
                    can_place_boat_check_1=True
        impossible_placement_check=check_all_directions(boat_lenght,boat_pos,all_boats_list)

    while not can_place_boat_check_2:
        direction=get_boat_direction(boat_lenght,boat_pos)
        current_try_pos=place_boat(boat_lenght,boat_pos,direction)
        for current_checking_boat_list in all_boats_list:
            for caracter in current_try_pos:
                if caracter in current_checking_boat_list:
                    can_place_boat_check_2=False
                    break
                else:
                    can_place_boat_check_2=True
    return current_try_pos