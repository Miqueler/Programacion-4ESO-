x=input()
vow=["a","e","i","o","u"]
if x.isupper(): print("uppercase")
else: print("lowercase")
if x.lower() in vow:
    print("vowel")
else:
    print("consonant")