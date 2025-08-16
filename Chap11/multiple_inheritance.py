class Employee:
    name = "Sarthak"
    company = "Microsoft"
    def show(self):
        print (f"The name is {self.name} and the salary is {self.salary}")
class Coder:
    language = "Python"
    def show(self):
        print (f"The name is {self.name} and the salary is {self.salary}")

class programmer(Employee,Coder): # Multiple inheritance
    def showlanguage(self):
        print(f"The programming language is {self.language}")

a = Employee()
b = programmer()

print(b.name, b.language)
print (a.name, a.company) # This will print "Sarthak Microsoft"