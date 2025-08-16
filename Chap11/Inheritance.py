class Employee:
    company = "Microsoft"
    language = "Python"
    def show(self):
        print (f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     def show (self):
#         print (f"The name is {self.name} and the salary is {self.salary}")
    
#     def show_programmer(self):
#         print (f"The name is {self.name} and the salary is {self.salary} and the programming language is {self.language}") 

class programmer(Employee):
    # company = "Google" # Uncommenting this line will override the company attribute in Employee class

    def showlanguage(self):
        print(f"The programming language is {self.language}")

a = Employee()
b = programmer()

print(a.language, b.language) # Both will print "Python" since b inherits from Employee