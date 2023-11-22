from game_main_logic import *
#1*5, 1*4, 2*3, 1*2
#Have to program check placed boats
all_boats_list=[]
boat_pos=get_boat_pos()
direction=get_boat_direction(3,boat_pos)
print(place_boat(3,boat_pos,direction))
