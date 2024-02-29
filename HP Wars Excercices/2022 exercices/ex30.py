x=""
teams=[]
bikers=[]
brands=[]
while x!=["#"]:
    x=input().split()
    if x!=["#"]:
        #Creates a list inside the bikers list with [biker_name,biker_points,biker's_team,biker's_brand]
        bikers.append([x[0],0,x[1],x[2]])
        if x[1] not in teams:
            teams.append([x[1],0])
        if x[2] not in brands:
            brands.append([x[2],0])
x=""
while x!="#":
    x=input()
    if x!="#":
        x=x.split("_")
        fast_lap=x[-1].split("|")
        x.pop(-1);x.append(fast_lap[0]);fast_lap.pop(0)
        point_rew=10
        for z in x:
            team=bikers[bikers.index(z)+2]
            brand=bikers[bikers.index(z)+3]
            bikers[bikers.index(z)+1]+=point_rew

            count_t=0
            while teams[count_t][0]!=team:
                count_t+=1
            brands[count_t][1]+=point_rew
            count_b=0
            while brands[count_b][0]!=brand:
                count_b+=1
                teams[count_b][1]+=point_rew


            if fast_lap in x:
                bikers[bikers.index(z)+1]+=1
                brands[count_t][1]+=1
                teams[count_b][1]+=point_rew
            if point_rew>4:
                point_rew-=2
            else:
                point_rew-=1

print(bikers)
print(brands)
print(teams)
