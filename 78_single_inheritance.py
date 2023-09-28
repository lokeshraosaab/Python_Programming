class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        # super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

a = Animal("Monty", "Dog")
a.make_sound()

d = Dog("Dog", "Doggerman")
d.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class.
#  Add some methods specific to cat

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        # super().__init__(name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        super().make_sound()
        print("Meow Meow!")

    def body_type(self):
        print("Having fur like hairs on the whole body")

c = Cat("Rani" , "Paltu Billi")
c.make_sound()
c.body_type()