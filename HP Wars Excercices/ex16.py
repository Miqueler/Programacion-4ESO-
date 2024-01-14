frase=input().split()
acr=[]
acr_start_pos=[]
counter =0

while counter<=len(frase)-1:
    first_letter= frase[counter][0]
    cons_upp=False
    if first_letter.isupper()==True:
        x=0
        temp_acr=""
        while True:
            try:
                next_letter=frase[counter+1][0]
            except IndexError:
                next_letter=""
            if next_letter=="":
                break
            elif next_letter.isupper():
                if x==0:
                    acr_start_pos.append(counter)
                    temp_acr=temp_acr+first_letter
                x+=1
                counter+=1
                temp_acr=temp_acr+next_letter
            else:
                break
        if x>0:
            acr.append(temp_acr)
    counter+=1

converted_frase=""
for i in frase:
    try:
        c_w=frase.index(i)
    except IndexError: break
    if c_w != acr_start_pos[0]:
        converted_frase+=i+" "
    else:
        converted_frase+=acr[0]+" " 
        acr_len=len(acr[0])
        acr.pop(0)
        for y in range(acr_len):
            try:
                frase.pop(c_w)
            except IndexError: pass

print(converted_frase)