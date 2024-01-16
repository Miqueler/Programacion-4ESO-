sentence=input().split()
pos_list=[]
while True:
    x=input()
    if x=="#":
        break
    else:
        pos_list.append(int(x)-1)
for i in range(len(pos_list)):
    y=sentence[pos_list[i]]
    final_word=""
    test=0
    for z in y:
        final_word+=y[-1-test]
        test+=1
    sentence[pos_list[i]]=final_word
    final_sentence=""
for i in sentence:
    final_sentence+=i+" "
print(final_sentence[:-1])