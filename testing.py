import time 
a=0
x=time.time()
while time.time()-x < 3:
    a+=1
print(a)