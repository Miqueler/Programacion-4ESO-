#Have to code a way to store the coords where boats have been hit
#The bot display only has to show where you have attacked and where you have hit

def print_map(hit_coords,boat_cooords,successfull_hits):
    map_layout=[["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"]]
    all_letters_map=["a","b","c","d","e","f","g","h","i","j"]
    for i in boat_cooords:
        for x in i:
            map_layout[int(x[0])][int(x[1])]="\x1b[3;32;40m@\x1b[0m"
    if hit_coords!=[]:
        for i in hit_coords:
            map_layout[int(i[0])][int(i[1])]="/"
    if successfull_hits!=[]:
        for i in successfull_hits:
                map_layout[int(i[0])][int(i[1])]="#"
    final_map=[]
    for z in map_layout:
        colored_map="["
        for i in z:
            if i=="@":
                colored_map+=f"\x1b[3;32;40m{i}\x1b[0m"+" ,"
            elif i=="/" or i=="#":
                colored_map+=f"\x1b[3;31;40m{i}\x1b[0m"+" ,"
            else:
                colored_map+=i+" ,"
        colored_map=colored_map[:-2]+"]"
        final_map.append(colored_map)

    print(" [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9,10]")
    y=0
    for i in final_map:
        print(f"{all_letters_map[y]}{i}")
        y+=1
    return map_layout

