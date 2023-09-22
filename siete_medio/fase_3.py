from random import randint

posible_nums=[1,2,3,4,5,6,7,10,11,12]
radn_num=-1
card=0
x=True
y=True
z=True
res_lit=[]
points=100


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
            print("You lost the game, better luck next time!")
            y=False
            res_lit.append(count)
            points-=10
            
        if count==7.5:
                print("Congratultions, you won the game!")
                y=False
                res_lit.append(count)
                points+=10
        if want_card!="0":
            if count <6:
                print("You could risk it a little more!")
                y=False
                res_lit.append(count)
                points-=5
                
            elif count in [6,6.5,7]:
                print("You were a little conservative!")
                y=False
                res_lit.append(count)
                points+=5
    while z:
        rand_num=randint(0,9)
        card=posible_nums[rand_num]
        if card in [10,11,12]:
            card=0.5

        if count>ban_count and count<7.5:
        
##Para a la banca si ya tiene una carta y el jugador se ha pasado
#        if count>7.5 and ban_count!=0:    
#            print(f"The bank got: {ban_count} points")
#            z=False
##Da carta si carta jugador es mayor que la de la banca y esta entre 5-7.5
#        if count>5 and count<=7.5 and count>ban_count:
#            ban_count+=card
##Se da la primera carta a la banca
#        if ban_count==0:
#            ban_count+=card
##Para banca si se pasa
#        if ban_count>7.5:
#            print(f"The bank got: {ban_count} points")
#            z=False
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
print(f"The result you got were: {res_lit}")