# Example of Hybrid Inheritance  # that is mixture of two or more than two type of inheritance
class BaseClass1:
  pass

class Derived1(BaseClass1):
  pass  

class Derived2(BaseClass1):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance # that is tree like structure
class BaseClass2:
  pass

class D1(BaseClass2):
  pass

class D2(BaseClass2):
  pass

class D3(D1):
  pass

class D4(D1):
  pass

class D5(D2):
  pass

class D6(D2):
  pass


