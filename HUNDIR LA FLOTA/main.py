from player_map_main_logic import *
from computer_map_main_logic import *
from player_main_game_fun import *
from computer_main_game_fun import *
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
bot_hits_list=[]
x=True
while x:
    current_player_hit=choose_hit(player_hits_list)
    player_hits_list.append(current_player_hit)
    player_hit_result=find_hit_result(bot_boat_placement,current_player_hit)

    
    if player_hit_result != "":
        print("Tocado")
        single_boat_list=bot_boat_placement[int(player_hit_result[0])]
        single_boat_list.pop(int(player_hit_result[1]))
        for i in bot_boat_placement:
            if i==[]:
                print("BARCO HUNDIDIO")
                bot_boat_placement.pop(bot_boat_placement.index(i))
                break
        if bot_boat_placement==[]:
            x=False
            print("You win, you have destroyed all the bot's boats!")

    current_bot_hit=bot_choose_hit(bot_hits_list)
    bot_hits_list.append(current_bot_hit)
    bot_hit_result=bot_find_hit_result(player_boat_placement,current_bot_hit)
    