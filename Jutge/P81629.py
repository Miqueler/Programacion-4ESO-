inp=input().split()
dol,cent=int(inp[0]),int(inp[1])
b5=0
b2=0
b1=0
b05=0
b02=0
b01=0
b005=0
b002=0
c5=0
c2=0
c1=0
c05=0
c02=0
if dol//500!=0: b5=dol//500; dol-=500*b5
if dol//200!=0: b2=dol//200; dol-=200*b2
if dol//100!=0: b1=dol//100; dol-=100*b1
if dol//50!=0: b05=dol//50; dol-=50*b05
if dol//20!=0: b02=dol//20; dol-=20*b02
if dol//10!=0: b01=dol//10; dol-=10*b01
if dol//5!=0: b005=dol//5; dol-=5*b005
if dol//2!=0: b002=dol//2; dol-=2*b002
if cent//50!=0: c5=cent//50; cent-=50*c5
if cent//20!=0: c2=cent//20; cent-=20*c2
if cent//10!=0: c1=cent//10; cent-=10*c1
if cent//5!=0: c05=cent//5; cent-=5*c05
if cent//2!=0: c02=cent//2; cent-=2*c02

print(f"""Banknotes of 500 euros: {b5}
Banknotes of 200 euros: {b2}
Banknotes of 100 euros: {b1}
Banknotes of 50 euros: {b05}
Banknotes of 20 euros: {b02}
Banknotes of 10 euros: {b01}
Banknotes of 5 euros: {b005}
Coins of 2 euros: {b002}
Coins of 1 euro: {dol}
Coins of 50 cents: {c5}
Coins of 20 cents: {c2}
Coins of 10 cents: {c1}
Coins of 5 cents: {c05}
Coins of 2 cents: {c02}
Coins of 1 cent: {cent}""")