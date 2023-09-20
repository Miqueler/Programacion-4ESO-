from random import randint

posible_nums=[1,2,3,4,5,6,7,10,11,12]
radn_num=-1
card=0
x=True
y=True
res_lit=[]
points=100
while x:
    count=0
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