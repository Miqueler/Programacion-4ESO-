from random import randint

def bot_get_boat_pos():
    boat_pos=""
    row=randint(0,9)
    index=randint(0,9)
    boat_pos+=str(row)
    boat_pos+=str(index)
    #Returns the position given as an index: first the row and then the index in line
    return boat_pos

def bot_check_all_directions(boat_lenght,boat_pos,all_boats_list):
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

def bot_get_boat_direction(boat_lenght,boat_pos):
    row=int(boat_pos[0])
    index=int(boat_pos[1])
    correct=False
    while not correct:
        direction=randint(0,3)
        if direction == 0:
            if row - boat_lenght>=0:
                correct=True
        elif direction == 1:
            if row + boat_lenght<=9:
                correct=True
        elif direction == 2:
            if index - boat_lenght>=0:
                correct=True
        elif direction == 3:
            if index + boat_lenght<=9:
                correct=True
    #Returs direction as a number up=0 down=1 left=2 right=3
    return direction

def bot_place_boat(boat_lenght,boat_pos,direciton):
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

def bot_check_if_placement_possible(all_boats_list,boat_lenght):
    can_place_boat_check_2=False
    impossible_placement_check=False
    while not impossible_placement_check:
        can_place_boat_check_1=False
        boat_pos=bot_get_boat_pos()
        while not can_place_boat_check_1 and all_boats_list!=[]:
            boat_pos=bot_get_boat_pos()    
            for i in all_boats_list:
                if boat_pos in i:
                    can_place_boat_check_1=False
                    break
                else:
                    can_place_boat_check_1=True
        if all_boats_list != []:
            impossible_placement_check=bot_check_all_directions(boat_lenght,boat_pos,all_boats_list)
        else:
            impossible_placement_check=True

    while not can_place_boat_check_2:
        direction=bot_get_boat_direction(boat_lenght,boat_pos)
        current_try_pos=bot_place_boat(boat_lenght,boat_pos,direction)
        if all_boats_list!=[]:
            for current_checking_boat_list in all_boats_list:
                for caracter in current_try_pos:
                    if caracter in current_checking_boat_list:
                        can_place_boat_check_2=False
                        break
                    else:
                        can_place_boat_check_2=True
        else: can_place_boat_check_2=True
    return current_try_pos