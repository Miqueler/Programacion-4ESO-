frases=[]
while True:
    x=input()
    if x=="#":
        break
    else:
        frases.append(x)

for i in range(len(frases)):
    current=frases[i].split()
    #try:
    #    next_frase=frases[i+1].split()
    #except IndexError: next_frase="0"
    if i==0:
        print("#"*len(max(current)))
    elif len(max(current))>len(max(frases[i-1].split())):
        print("#"*len(max(current)))
    for x in current:
        print("#"+x+(" "*len(max(current)))-len(x)+"#")