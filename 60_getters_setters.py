class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
# @property decorator use krne se given function prperty ki trh use hone lgta h but ise change nhi kr skte
#   mtlb ki yh getter bn gya h 
  @property  
  def ten_value(self):
      return 10* self._value

# ab neeche diya gya syntax setter bnaane ke liye h ab ise change bhi kr skte hai 
# ten_value yha ab new value ki trh jayegi  
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()