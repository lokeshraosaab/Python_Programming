class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y
  
rec = Shape(3, 5)
print(rec.area())

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    
c = Circle(5)
print(c.area())