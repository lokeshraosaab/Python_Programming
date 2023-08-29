# average function
# Required arguements

# def average(a, b):
#   print("The average is ", (a + b) / 2)

# average(4, 6)

# ways of passing values to the function

# def average(a=3, b=4):
#   print("The average is ", (a + b) / 2)

# average() # default arguemnts
# average(5,6)
# average(5) # take remaining arguements as defualt as given
# average(b=5)
# average(b=9, a=3) # keyword arguements order does not matter

# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)

# average(2, 3)


def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
#   print("Average is: ", sum / len(numbers))
#   return 7
  return sum / len(numbers)

# average(2, 4, 5, 6, 7)

c = average(2, 4, 5, 6, 7)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname="Buchanan", lname="Barnes", fname="James")

