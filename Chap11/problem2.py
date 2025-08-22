class animal():
    pass

class pet(animal):
    pass

class dog(pet):
    
    @staticmethod # Static method as it does not use self parameter 
    def bark():
        return "bhow bhow!"
    
d= dog()
print(d.bark())

