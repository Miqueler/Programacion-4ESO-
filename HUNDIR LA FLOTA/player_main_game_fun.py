def choose_hit(hits_list):
    check=False
    while not check:
        hit_coord=""
        row=""
        all_letters_map=["a","b","c","d","e","f","g","h","i","j"]
        while row not in all_letters_map:
                row=input("What row do you want to hit (a-j): ")
        row=all_letters_map.index(row)
        corr=False
        x=""
        while corr==False:
            x=input("What vertical row do you want to hit (1-10): ")
            if x.isnumeric():
                index=int(x)-1
                if index>=0 and index<=9:
                    corr=True
        hit_coord+=str(row)     
        hit_coord+=str(index)
        if hit_coord not in hits_list:
            check=True
    return hit_coord

#Returns if the boat was hit as True=Hit and False=Water
def find_hit_result(bot_all_boats_list,hit_coord):
    hit_result=""
    for i in bot_all_boats_list:
        if hit_coord in i:
            hit_result=str(bot_all_boats_list.index(i))+str(i.index(hit_coord))
            break
    return hit_result
