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
    for i in boat_cooords:
        for x in i:
            map_layout[int(x[0])][int(x[1])]="@"
    if hit_coords!=[]:
        for i in hit_coords:
            map_layout[int(i[0])][int(i[1])]="/"
    if successfull_hits!=[]:
        for i in successfull_hits:
                map_layout[int(i[0])][int(i[1])]="#"
    for i in map_layout:
        print(i)
    return map_layout

