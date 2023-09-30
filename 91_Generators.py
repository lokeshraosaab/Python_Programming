# The yield statement returns a value from the generator
#  and suspends the execution of the function until the next value is requested.

def my_generator():
    for i in range(5):
      # Complex computations
      yield i

gen = my_generator()

# The next() function is used to request the next value from the generator, 
# and the generator resumes its execution until it encounters another yield statement 
# or until it reaches the end of the function.

# print(next(gen))
# print(next(gen))
# print(next(gen))

print("Now using loop")
# he generator is used to generate the values one-by-one 
# as the loop iterates over it.
# if gen is already called before using next or directly then it will be resumed here 

for j in  gen:
  print(j)