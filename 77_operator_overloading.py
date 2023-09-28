class Vector:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x): # yhh objects ke beech m add dikhne se call ho jayega sutomatically bcz yhh dunder h
    return Vector(self.i + x.i,  self.j+x.j, self.k+x.k) # yhh as a nya vector class ko call krega
  
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)
print(type(v1 + v2))
# it is like 
# v3 = v1 + v2
# yha v3 __add__ call hone se aesa ho jayega v3 = Vector(4,7,15)
# print(v3)
# print(type(v3))
