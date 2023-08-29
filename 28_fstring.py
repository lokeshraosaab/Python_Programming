letter = "Hey my name is {} and I am from {}"
# letter = "Hey my name is {1} and I am from {0}"
# print(letter.format(country, name))
country = "India"
name = "Harry"

# string formatting using format
print(letter.format(name, country))
print(letter.format(country, name))

# string formatting using f-string
print(f"Hey my name is {name} and I am from {country}")

# this is another way for string formatting
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.6008))

# doing same using f-string
price = 50.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

# retains curly braces in f string : use double curly braces
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")