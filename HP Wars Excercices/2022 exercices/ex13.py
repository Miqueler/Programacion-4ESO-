#from math import ceil
#x=input()
#abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#total=int()
#if x.isnumeric():
#    fin=""
#    if int(x)<=26:
#        print(abc[int(x)-1])
#    else: 
#        x=int(x)
#        div=x/26
#else:
#    if len(x)==1:
#        print(abc.index(x)+1)
#    else:
#        for i in range(len(x)):
#            f=i+1
#            total+=(abc.index(x[i])+1)*26**(len(x)-f)
#        print(total)

def number_to_base26(num):
    """
    Convert a positive number to its corresponding base-26 system string.
    """
    if num == 0:
        return 'A'
    
    base26_string = ''
    while num > 0:
        num -= 1
        remainder = num % 26
        base26_string = chr(remainder + ord('A')) + base26_string
        num //= 26
    return base26_string

def base26_to_number(base26_string):
    """
    Convert a base-26 system string to its corresponding positive number.
    """
    num = 0
    for char in base26_string:
        num = num * 26 + (ord(char) - ord('A') + 1)
    return num

def convert(input):
    """
    Convert input between positive numbers and base-26 system strings.
    """
    if isinstance(input, int) or isinstance(input, float):
        return number_to_base26(input)
    elif isinstance(input, str):
        return base26_to_number(input)
    else:
        return None

# Test the conversion functions
print(convert(123))  # Output: 'ABCD'
print(convert('A')) # Output: 19010
