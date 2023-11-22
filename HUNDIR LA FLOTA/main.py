from game_main_logic import *
#1*5, 1*4, 2*3, 1*2
#Have to program check placed boats
#Check if position is impossible for boat
all_boats_list=[]
b5=1
b4=1
b3=2
b2=1
can_place_boat_check=False
can_place_boat_check_1=False
can_place_boat_check_2=False
#We place the 5 lenghth boat
boat_pos=get_boat_pos()
direction=get_boat_direction(5,boat_pos)
single_5_boat=place_boat(5,boat_pos,direction)
all_boats_list.append(single_5_boat)
#We place the 4 lenght boat checking for no interfearence with the previous ones
while not can_place_boat_check:
    while not can_place_boat_check_1:
        boat_pos=get_boat_pos()
        for i in all_boats_list:
            if boat_pos in i:
                can_place_boat_check_1=False
            else:
                can_place_boat_check_1=True
    while not can_place_boat_check_2:
        direction=get_boat_direction(3,boat_pos)
        current_try_pos=place_boat(3,boat_pos,direction)
        for current_checking_boat_list in all_boats_list:
            for caracter in current_try_pos:
                if caracter in current_checking_boat_list:
                    can_place_boat_check_2=False
                else:
                    can_place_boat_check_2=True
    can_place_boat_check=True
