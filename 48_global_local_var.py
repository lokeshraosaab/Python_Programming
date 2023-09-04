# x = 4
# print(x)

# def hello():
#     x = 5
#     y = 1
#     print(f"The local x is {x}")


# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")
#  # print(y) # it throws error as y is not global variable so it can be accessible only from the function where it is defined
#  # It is created when the function is called and is destroyed when the function returns.
#  # On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code

x = 10  # global variable
z = 8

def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 7  # local variable
  z = 6  # Here it is local variable


my_function()
print(x)  # prints 5 instead of 10
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
print(z)  # print the same value as it was