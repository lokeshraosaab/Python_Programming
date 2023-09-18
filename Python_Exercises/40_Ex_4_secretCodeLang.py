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




        




  