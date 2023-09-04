# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

# st = input("Enter message : ")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# Syntax : random.choices(sequence, weights=None, cum_weights=None, k=1)

# Parameters :
# 1. sequence is a mandatory parameter that can be a list, tuple, or string.
# 2. weights is an optional parameter which is used to weigh the possibility for each value.
# 3. cum_weights is an optional parameter which is used to weigh the possibility for each value but in this the possibility is accumulated
# 4. k is an optional parameter that is used to define the length of the returned list.

import string
import random

def coding():
    message = input("Enter Your message here : ")
    words = message.split(" ") # Here it will split the message by the space in different words and returns the list of substrings
    cwords = [] # Here it is an empty list
    for word in words :
        if(len(word)>=3):
            r1 = random.choices(string.ascii_lowercase, k=3) # r1,r2 are lists contains random generated 3 strings of a lowescase 
            r2 = random.choices(string.ascii_lowercase, k=3)
            code = "".join(r1) + word[1:] + word[0] + "".join(r2)
            cwords.append(code)  # Here cwords will contain every code as element of list
        else :
            cwords.append(word[::-1])
    
    print("Your coded message is here :")
    print(" ".join(cwords)) # Here first it will join the elements of the list cwords by space and then print it

def decoding():
    code = input("Enter the coded message to be decode : ")
    words = code.split(" ")
    dwords = []
    for word in words :
        if(len(word)>=3):
            decode =word[-4] + word[3:-4]
            dwords.append(decode)
        else :
            dwords.append(word[::-1])

    print("Your decoded message is here : ")
    print(" ".join(dwords))


try :
    print("Enter Your Input first , 1 for coding , 2 for decoding and 0 for quit ")
    a = int(input("Now Enter : "))
    if a == 1 :
        coding()
    elif a == 2 :
        decoding()
    elif a == 0 :
        print("Thanks Ok")
except :
    print("Invalid Input")




        




  