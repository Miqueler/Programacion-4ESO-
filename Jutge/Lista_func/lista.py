#Write a function myLength(L) that, given a list, returns its length.
#Write a function myMaximum(L) that, given a non-empty list, returns its maximum
#Write a function average(L) that, given a non-empty list of numbers, returns its average
#Write a function buildPalindrome(L) that, given a list, returns the palindrome that starts with the reverse of the list
def myLenghth(L):
    return len(L)

def myMaximum(L):
    return max(L)

def average(L):
    return sum(L)/len(L)

def buildPalindrome(L):
    return L+list(reversed(L))


a=[1,3,6,1]
b=[4,3,1,5,4,5,2]
c=['josep', 'jordi', 'albert']
d=[1,2,3]
e=["pa", "oli", "sal"]

print(myLenghth(a))
print(myMaximum(b))
print(average(d))
print(buildPalindrome(e))