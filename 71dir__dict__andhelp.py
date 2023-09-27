x = [1,2,3]
print(dir(x))
print(x.__add__)

print("\n")

x = (1,2,3)
print(dir(x))
print(x.__add__)

print("\n")

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.version = 1

P1 = Person("Dileep", 30)
print(P1.__dict__)

print("\n")

print(help(Person))