a = 4
b = "4"
print(a is b) # returns False as here a and b are not same object in memory
print(a == b) # returns False a and b are not same in value
# print(f"{a==b} \n") # returns False a and b are not same in value
print("\n")

a = [1,4,43]
b = [1,4,43]
# lists are mutable 
# so every time for same lists it will take memory separetely
print(a is b) # returns False as a and b are lists but created separately
print(a == b) # returns True as a and b , both have same values 
print("\n")

a = 3
b = 3
# here 3 is constant it will not change so in memory it will created once. same for strings
print(a is b) # returns True
print(a == b) # returns True
print("\n")

a = (1,2)
b = (1,2)
# tuples are immutable , same as strings and constant values
print(a is b) # returns True
print(a == b) # returns True
print("\n")

a = None
b = None

print(a is b) # returns True
print(a is None)
print(b is None)
print(a == b) # returns True
print("\n")

# in outputs there is gap of two lines bcz print will return you next line after return
# and then we are using \n means (skip this line) with another print that will return first skip line and command will go to next line 
# and here print return command to the next line