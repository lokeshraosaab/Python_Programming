class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("This is the parent method of ChildClass.")

    def child_method(self):
        print("This is the child method.")
        super().parent_method() # super keyword lgne se hmesha parent class ka method hi call hoga

child_object = ChildClass()
child_object.child_method()
child_object.parent_method() # agr child class m given method nhi h tb parent class ka method call hoga