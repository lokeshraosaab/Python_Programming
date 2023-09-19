class Employee :
    CompanyName = "Apple" # Here it is class variable so it will be same for all the instances 
    # untill instance variable is not created as CompanyName for the particular instance
    # it is class associative
    # and so it can be change only by class.
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 
        Employee.noOfEmployees +=1
        #here name and raise_amount are instance associative in nature. So these are instance variable.
        # and it can be change according to the instance
    def ShowDetails(self) :
        print(f"The name of the employee is {self.name} and the raise amount in {self.CompanyName} sized {self.noOfEmployees} is {self.raise_amount}")
    def MoreDetails(self) :
        print(f"Employee ID of {self.name} is {self.ID} and location is {self.CompanyLoc}")
emp1 = Employee("Lokesh")
emp1.name = "Rohan"
emp1.raise_amount = 0.3 
#these changes will be reflect in the output bcz these are instance associative in nature.
#So can be change using instance.
emp1.ShowDetails() # Here company name will be shown as it is given as class associative variable CompanyName
# Employee.ShowDetails(emp1) # that is same as emp1.ShowDetails()

emp2 = Employee("Ankit")
emp2.ShowDetails() # Here company name will be shown as it is given as class associative variable CompanyName

emp3 = Employee("Shivam")
emp3.CompanyName = "Apple India" # Here a Instance variable created same as class variable CompanyName
emp3.ShowDetails() # Here company Name will be shown as new name as given by same instance variable 

Employee.CompanyName = "Google" # class variable can be change only by class 
emp1.ShowDetails() # Google 
emp2.ShowDetails() # Google
emp3.ShowDetails() # Apple India

emp1.ID = 10 # we can create instance variable out of the class
emp2.ID = 20
emp3.ID = 30
Employee.CompanyLoc = "Noida" # we can create class variable out of the class
emp1.MoreDetails()
emp2.MoreDetails()
emp3.MoreDetails()

