from player_map_main_logic import *
from computer_map_main_logic import *
from player_main_game_fun import *
import time
#1*5, 1*4, 2*3, 1*2
#Have to program check placed boats
#Check if position is impossible for boat
player_boat_placement=[]
#boat_pos=get_boat_pos()
#direction=get_boat_direction(5,boat_pos)
#player_boat_placement.append(place_boat(5,boat_pos,direction))
#player_boat_placement.append(check_if_placement_possible(player_boat_placement,4))
#player_boat_placement.append(check_if_placement_possible(player_boat_placement,3))
#player_boat_placement.append(check_if_placement_possible(player_boat_placement,3))
#player_boat_placement.append(check_if_placement_possible(player_boat_placement,2))
#print(player_boat_placement)

time_start=time.time()
bot_boat_placement=[]
bot_boat_placement.append(bot_check_if_placement_possible(bot_boat_placement,5))
bot_boat_placement.append(bot_check_if_placement_possible(bot_boat_placement,4))
bot_boat_placement.append(bot_check_if_placement_possible(bot_boat_placement,3))
bot_boat_placement.append(bot_check_if_placement_possible(bot_boat_placement,3))
bot_boat_placement.append(bot_check_if_placement_possible(bot_boat_placement,2))
print(bot_boat_placement)
print(time.time()-time_start)

player_hits_list=[]
current_player_hit=choose_hit(player_hits_list)
player_hits_list.append(current_player_hit)
player_hit_result=find_hit_result(bot_boat_placement,current_player_hit)
print(player_hit_result)