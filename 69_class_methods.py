class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

# This method is not class method but here we create a method which will change the company 
# name for the desired employee but it can't be change the class company name

  def changecompanyofemp(cls, newcompanyname):
    cls.company = newcompanyname

# To define a class method, you simply use the "@classmethod" decorator before the method definition.
# The first argument of the method should always be "cls," which represents the class itself
# with the help of class methods we can change the company name or we can say we can change class variables using any instances
 
  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()

e1.changecompanyofemp("Samsung")
e1.show()
print(Employee.company)

e1.changeCompany("Tesla") #Here only name of the company for the class will be change 
                          #we have already change employee company using another method
                          #if we are not using any other method for the change of employee company name
                          # then samw change will be reflect in both class company name and employee company name
e1.show()
print(Employee.company)