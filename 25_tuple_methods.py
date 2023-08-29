# countries = ("Spain", "Italy", "India", "England", "Germany")
# print(countries)
# temp = list(countries)
# temp.append("Russia")       #add item 
# print(temp)
# temp.pop(3)                 #remove item
# print(temp)
# temp[2] = "Finland"         #change item
# print(temp)
# countries = tuple(temp)
# print(countries)

# in concatenation there is formation of new tuple from given two tuples
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
print(tuple1.count(3))
print(tuple1.index(31))
print(tuple1.index(3))
print(len(tuple1))
# print(tuple1.index(311)) # throws error as 311 is not in tuple
print(tuple1.index(3, 4, 8)) # returns the index of 3 that is in between the index 4 and 8


