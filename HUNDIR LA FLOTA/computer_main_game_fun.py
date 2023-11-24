from random import randint

def bot_choose_hit(hits_list):
    check=False
    while not check:
        hit_coord=""
        row=randint(0,9)
        index=randint(0,9)
        hit_coord+=str(row)     
        hit_coord+=str(index)
        if hit_coord not in hits_list:
            check=True
    return hit_coord

#Returns if the boat was hit as True=Hit and False=Water
def bot_find_hit_result(player_all_boats_list,hit_coord):
    hit_result=""
    for i in player_all_boats_list:
        if hit_coord in i:
            hit_result=str(player_all_boats_list.index(i))+str(i.index(hit_coord))
            break
    return hit_result