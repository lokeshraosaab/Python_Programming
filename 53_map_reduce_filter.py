# ##### MAP #####  map(function, iterable)
# def cube(x):
#   return x * x * x

# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# newl = list(map(cube, l))
# print(l)
# print(newl)

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Double each number using the map function
# doubled = map(lambda x: x * 2, numbers)

# # Print the doubled numbers
# print(numbers)
# print(list(doubled))

# ##### FILTER #####  filter(predicate, iterable) , predicate function :- it returns boolean value only
# def filter_function(a):
#   return a>2
  
# newnewl = list(filter(filter_function, l))
# print(newnewl)

# ##### Reduce #####  reduce(function, iterable) , first we have to import from functools

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
# Here , how is the reduce function works
# numbers = [1, 2, 3, 4, 5]
# numbers = [3,3,4,5]
# numbers = [6,4,5]
# numbers = [10,5]
# numbers = [15]

# Print the sum
print(sum) 