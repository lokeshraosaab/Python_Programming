# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

a = True
print(a)
print(a := False)

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

print("\n")

# # That is without using walrus operator
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

# print(foods)

# # That is with using walrus operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)
