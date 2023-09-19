# Static methods in Python are methods that belong to a class 
# rather than an instance of the class

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod # iska mtlb h method create krne ke liye self arguement dena jroori nhi h
  def add(a, b):
      return a + b

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(7, 2))  # object ka use krke bhi call kr skte hai

result = Math.add(1, 2) # direct class ke through bhi use kr skte hai
print(result) # Output: 3