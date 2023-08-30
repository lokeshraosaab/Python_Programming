for i in range(5):
    print(i)

else :
    print("Sorry No i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

for i in []:
    print(i)

else :
    print("Sorry No i")

for i in range(6):
    print(i)
    if i==4 :
        break

else :                      # yhaa else execute nhi hoga bcz for ya while ke sath else ka execute hona loop khtm hone pr depend h only break hona alg baat h
    print("Sorry No i")  

i=0 
while i<7 :
    print(i)
    if i==4 :
        break
    i=i+1

else:
    print("Sorry No i")  