dif=input()
n_mines=int(input())
coords=[]
for i in range(n_mines):
    coords.append(input())
e_map=[[0,0,0],[0,0,0],[0,0,0]]
m_map=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
h_map=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
def place_mines(map,mines):
    for i in mines:
        map[int(i[0])-1][int(i[-1])-1]="#"
    return map
def change_heat(map):
    c_list=0
    c_point=0
    for i in map:
        c_point=0
        for x in i:
            if x=="#":
                try:
                    if map[c_list][c_point+1]!="#":
                        map[c_list][c_point+1]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if c_point-1>=0:
                        if map[c_list][c_point-1]!="#":
                            map[c_list][c_point-1]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if map[c_list+1][c_point]!="#":
                        map[c_list+1][c_point]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if c_list-1 >=0:
                        if map[c_list-1][c_point]!="#":
                            map[c_list-1][c_point]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if map[c_list+1][c_point+1]!="#":
                        map[c_list+1][c_point+1]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if c_point-1 >=0:
                        if map[c_list+1][c_point-1]!="#":
                            map[c_list+1][c_point-1]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if c_list-1>=0:
                        if map[c_list-1][c_point+1]!="#":
                            map[c_list-1][c_point+1]+=1
                except IndexError or TypeError:
                    pass
                try:
                    if c_list-1>=0 and c_point>=0:
                        if map[c_list-1][c_point-1]!="#":
                            map[c_list-1][c_point-1]+=1
                except IndexError or TypeError:
                    pass
            c_point+=1
        c_list+=1
    return map
if dif=="Hard":
    t_map=h_map
elif dif=="Easy":
    t_map=e_map
elif dif=="Medium":
    t_map=m_map
mined_map=place_mines(t_map,coords)
final_map=change_heat(mined_map)
for i in final_map:
    temp=""
    for x in i:
        temp+=str(x)
    print(temp)
