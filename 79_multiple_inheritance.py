class Employee:
  def __init__(self, name, id):
    self.name = name
  def show(self):
    print(f"The name is {self.name} and the id is {self.id}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    Employee.show(self)
    print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
class DancerEmployee(Dancer, Employee): # The order of multiple classes to be inherit matters
  def __init__(self, name, dance, id):
    self.dance = dance
    self.name = name
    self.id = id

o  = DancerEmployee("Shivani", "Kathak", 77)
# print(o.name)
# print(o.dance)
# print(o.id)
o.show()
print(DancerEmployee.mro()) # mro() method resolution order shows the order of searching of the method called by the object of child class