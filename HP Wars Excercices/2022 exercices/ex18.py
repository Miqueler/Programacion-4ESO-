frases=[]
while True:
    x=input()
    if x=="#":
        break
    else:
        frases.append(x)

for i in range(len(frases)):
    current=frases[i].split()
    if i==0:
        print("#"*(len(max(current))+4))
    elif len(max(current))>len(max(frases[i-1].split())):
        print("#"*(len(max(current))+4))
    else:
        print("#"*(len(max(frases[i-1].split()))+4))
    for x in current:
        print("# "+x+(" "*(len(max(current))-len(x)))+" #")

print("#"*(len(max(current))+4))