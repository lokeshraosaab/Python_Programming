class employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    
    def __call__(self):
        return "Hey I am Good"
    
e = employee("Harry")

print(e.name)
print(len(e))

print(e) # returns __str__ if there is no str then it will look upto repr and print repr
print(str(e))
print(repr(e))
print(e())
