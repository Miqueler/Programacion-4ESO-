num=int(input())
#idk pto sheldon
flag=False
def reverse_num(num):
    final=str()
    for i in str(num):
        final= i+final
        return final

def is_prime(num):
    flag=False
    if num==1:
        flag=True
    else:
        for i in range(2,int(num)):
            if int(num)%i==0:
                flag=True
                break
    return flag
def prime_pos(num):
    x=0
    pos=0
    while x!=num:
        x+=1
        if is_prime(num):
            pos+=1
    return pos

prime=is_prime(num)
mirr=reverse_num(num)
mirr_pr=is_prime(mirr)
pos=prime_pos(num)
mirr_pos=prime_pos(mirr)

if prime ==False:
    if mirr_pr==False:
        if pos==reverse_num(mirr_pos):
            print(f"Number {num} is a Sheldon prime!")
        elif sorted(list(pos))==sorted(list(mirr_pos)):
            print(f"Number {num} is a Sheldon prime relative")
        elif is_prime(pos)==False and is_prime(mirr_pos)==False:
            print(f"Number {num} is a close friend of Sheldon prime")
        else:
            print(f"Number {num} is a friend of Sheldon prime")
    else:
        print(f"Number {num} is not related to Sheldon prime")
else:
    print(f"Number {num} is not related to Sheldon prime")