# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
double = lambda x: x * 2
# Lambda function to cube the input
cube = lambda x: x * x * x
# Lambda function for avg of the three input
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(5, 6, 7))

# function ko bhi function pass krr ske aesa ek function bnaa leinge
def appl(fx, value) :
    return 6 + fx(value)


# function ko bhi function pass krr skte hai as a arguement like this
print(appl(cube, 3))
# lambda function ka naam nhi hota h , hmne cube , avg , double bss de diya h behaviour ke according
print(appl(lambda x : x*x*x*x , 2))
print(appl(lambda x : x*x , 2))

# Lambda function to calculate the product of two numbers,
# with additional print statement
product = lambda x, y: print(f'{x} * {y} = {x * y}')
product(9,5)

