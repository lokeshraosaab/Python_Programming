l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

# list is updated after every method we applied to the list

# l.append(7)
# print(l)

# l.sort() # sort in ascending order
# print(l)

# l.sort(reverse = True) # sort in descending order
# print(l)

# l.reverse() # reverse the order of lists
# print(l)

# print(l.index(6))
# print(l.count(1))

# m = l.copy()
# m[0] = 0
# print(l) # l vhi rhegi jo thi bcz copy method use kiya h

# m = l
# m[0] = 0
# print(l)  # yha l m bhi change ho jayega bcz m = l reference de diya h acc to pyhton

# l.insert(1, 899)
# print(l)

m = [900, 1000, 1100]

k = l+m
print(k) 

l.extend(m)
print(l)