class Employee:
    a = 1
    
    @classmethod # Class method to access class attribute
    def show(cls):
        print(f"The class attribute of a is {cls.a}") # Class method to access class attribute

    @property       # Property decorator to manage name as a single attribute
    def name(self):
        return f"{self.fname} {self.lname}" 
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0] # Assuming two parts only
        self.lname = value.split(" ")[1] # Assuming two parts only

e = Employee()
e.a = 45  

e.name = "Harry Khan"
print(e.fname, e.lname) # This will print "Harry Khan"

e.show() # This will print the class attribute a, which is 1