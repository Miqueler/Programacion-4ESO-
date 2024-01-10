from random import choice

test=[1,1,1,1,2,2,2,2,3,3,3,3]

x=choice(test)
test.pop(test.index(x))
print(test)