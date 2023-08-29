# tup = (1,2,3)
# print(type(tup), tup)
# tup = (1,2)
# print(type(tup), tup)
# tup = (1,)
# print(type(tup), tup)
# tup = (1)  # Here class type is int bcz tuple takes multiple values always with one value comma is necessary to be called tuple
# print(type(tup), tup)

# tuples, strings are unchangeable means immutable whereas lists are changeable means mutable
# tup[0]=100  # this will throw error for tuple as this assignment does not support by tuple
# print(tup)

# lst = [1, 2, 3]
# lst[0] = 100
# print(lst)

tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
# print(tup[34]) # throws error index is out of range
print(len(tup))
print(tup[-1])
print(tup[-3])
print(tup[1:4])
print(tup[0:3])

if  342 in tup:
  print("Yes 342 is present in this tuple")
else :
  print("No")
tup2 = tup[1:4]
print(tup2)