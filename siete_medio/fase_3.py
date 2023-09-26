from random import randint
#Missing: add the display of the results
posible_nums=[1,2,3,4,5,6,7,10,11,12]
radn_num=-1
card=0
x=True
y=True
z=True
res_lit=[]
ban_res_list=[]
points=100
wins_ban=0
los_ban=0
draw_ban=0

while x:
    count=0
    ban_count=0
    
    while y:
        rand_num=randint(0,9)
        card=posible_nums[rand_num]
        if card in [10,11,12]:
            card=0.5

        
        want_card=input("If you want a card type 0: ")
        if want_card=="0":
            count+=card
            print(f"Your card was: {card}")
            print(f"Your current card count is: {count}")

        if count>7.5:
            y=False
            res_lit.append(count)
            points-=10
            
        if count==7.5:    
                y=False
                res_lit.append(count)
                points+=10
        if want_card!="0":
            if count <6:               
                y=False
                res_lit.append(count)
                points-=5  
            elif count in [6,6.5,7]:  
                y=False
                res_lit.append(count)
                points+=5
    #The bank
    while z:
        rand_num=randint(0,9)
        card=posible_nums[rand_num]
        if card in [10,11,12]:
            card=0.5

        if count>ban_count and count<7.51:
            ban_count+=card
            print(f"The bank got a {card}")
        elif ban_count==0:
            ban_count+=card
            print(f"The bank got a {card}")
        elif count==ban_count and count>=5:
            ban_count+=card
            print(f"The bank got a {card}")

        else:
            z=False
            print(f"The final bank count is {ban_count}")
            ban_res_list.append(ban_count)
    if count>7.5:
        print("You lost, the bank beat you!")
        los_ban+=1
    elif ban_count>count and ban_count<7.51:
        print("You lost, the bank beat you!")
        los_ban+=1
    elif ban_count<count and count < 7.51:
        print("You beat the bank!")
        wins_ban+=1
    elif count==ban_count:
        print("This is a draw!")
        draw_ban+=1
    elif ban_count>7.5 and count>7.5: 
        print("You both lost!")
        los_ban+=1
    elif ban_count>7.5 and count <=7.5:
        print("You beat the bank!")
        wins_ban+=1

    if points<=0:
        x=False    
        print("You ran out of points, better luck next time")
    else:
        finisher=input("If you want to end the game type end: ")
        if finisher=="end":
            x=False
            print(f"Nice game, you got {points} points!")
        else:
            y=True
            z=True
print(f"The results you got were: {res_lit}")
print(f"The results the bank got were: {ban_res_list}")