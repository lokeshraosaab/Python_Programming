s = {2, 4, 2, 6}
print(s)  # set repeated values nhi leta h

info = {"Carla", 19, False, 5.9, 19}
print(info) #Sets are unordered collection of data items print hone ka order jroori nhi jo diya h vhi ho
# kisi bhi order m dekhne ko mil skta h ....bcz set order maintain nhi krta h 

harry = {}  # this is not the empty set this is dictionary here actually
print(harry)
print(type(harry))

harry = set() # this is empty set and this syntax of set is valid only for at most 1 arguement
print(harry)
print(type(harry))

harry = set("a") # here is only one arguement so this is also valid but only for string input
# harry = set(1) # throws error
print(harry) # output {'a'}
print(type(harry))

harry = {"a"}
print(harry) # output {'a'}
print(type(harry))

harry = {1}
print(harry) # output {'1'}
print(type(harry))

for value in info:
  print(value)


