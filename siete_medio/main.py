from random import randint

posible_nums=[1,2,3,4,5,6,7,10,11,12]
radn_num=-1
card=0
x=True
y=True
res_lit=[]
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
            print(f"Your current card count is: {count}")

        if count>7.5:
            print("You lost the game, better luck next time!")
            y=False
            res_lit.append(count)
        if count==7.5:
                print("Congratultions, you won the game!")
                y=False
                res_lit.append(count)
        if want_card!="0":
            if count <6:
                print("You could risk it a little more!")
                y=False
                res_lit.append(count)
            elif count in [6,6.5,7]:
                print("You were a little conservative!")
                y=False
                res_lit.append(count)
        


    finisher=input("If you want to end the game type end: ")
    if finisher=="end":
        x=False
    else:
        y=True
print(f"The result you got were: {res_lit}")