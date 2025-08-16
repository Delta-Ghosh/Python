# Base class (Grandparent)
class Animal:
    animal_type = "Mammal"
    def speak(self):
        print("Animals make sounds")

# Derived class (Parent)
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Derived from Dog (Child)
class Puppy(Dog):
    def speak(self):
        print("Puppy yaps")

# Create objects
a = Animal()
d = Dog()
p = Puppy()

# Call methods
a.speak()   # From Animal
d.speak()   # From Dog
p.speak()   # From Puppy
