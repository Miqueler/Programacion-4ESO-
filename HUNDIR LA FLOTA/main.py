from game_main_logic import *
#1*5, 1*4, 2*3, 1*2
#Have to program check placed boats
#Check if position is impossible for boat
all_boats_list=[]
#We place the 5 lenghth boat
boat_pos=get_boat_pos()
direction=get_boat_direction(5,boat_pos)
single5=place_boat(5,boat_pos,direction)
all_boats_list.append(single5)
#We place the 4 lenght boat checking for no interfearence with the previous ones
single4=check_if_placement_possible(all_boats_list,4)
all_boats_list.append(single4)
#We place the 3 lenght boats checking for no interfearence with the previous ones
single3_1=check_if_placement_possible(all_boats_list,3)
all_boats_list.append(single3_1)
single3_2=check_if_placement_possible(all_boats_list,3)
all_boats_list.append(single3_2)
#We place the 3 lenght boats checking for no interfearence with the previous ones
single2=check_if_placement_possible(all_boats_list,2)
all_boats_list.append(single2)
print(all_boats_list)
