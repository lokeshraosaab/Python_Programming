# PUBLIC ACCESS MODIFIERS 
# All the variables and methods (member functions) in python are by default public
# Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

class Student:
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)

# PRIVATE ACCESS MODIFIERS
# a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__).
# This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. 
# Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

class Employee:
    def __init__(self):
        self.__name = "Lokesh"

a = Employee()
# print(a.__name) # Cannot be acceses directly
print(a._Employee__name) # But can be access using obj._classname__variable # that is called name mangling 
# print(a.__dir__())

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

# PROTECTED ACCESS MODIFIER
# It's important to note that the single underscore is just a naming convention, 
# and does not actually provide any protection or restrict access to the member.

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
# print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
