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
            map_layout[int(x[0])][int(x[1])]="@"
    if hit_coords!=[]:
        for i in hit_coords:
            map_layout[int(i[0])][int(i[1])]="/"
    if successfull_hits!=[]:
        for i in successfull_hits:
                map_layout[int(i[0])][int(i[1])]="#"
    print(" [/1/ ,/2/ ,/3/ ,/4/ ,/5/ ,/6/ ,/7/ ,/8/ ,/9/,/10/]")
    y=0
    for i in map_layout:
        print(f"{all_letters_map[y]}{i}")
        y+=1
    return map_layout

