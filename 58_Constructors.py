class person :
    name = "Harry"
    occ = "Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person()
# print(a.name)
a.name = "Lokesh"
a.occ = "HR"
a.info()

class Person:
  # parametrized constructor 
  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")

# constructor is invoked automatically when a object of a class is created
# that's why "Hey I am a person " prints , when object created
# when constructor is used then when we create object arguments will be pass other than self
# object is automatically passes as self without mentioning anywhere.

a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
# c = Person(1,2,3) # it will show error as we are passing 4 arguements out of them 3 are showing but object is also passing as self
a.info()
b.info()

class Details:
  # Default constructor
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")

obj1=Details()

