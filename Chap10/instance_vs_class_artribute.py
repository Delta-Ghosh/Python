class employee:
    salary = 100000 #THis is a class attribute
    lamguage = "Python"

    def getinfo(self): # This is a method to print employee info 
        #slef is the instance of the class and it is used to access the attributes and methods of the class.
        print (f"The Salary is : {self.salary}. \nKnown Language is : {self.lamguage}") # This is a method to print employee info
        
    @staticmethod
    def greet(): #static method to greet the employee
        print("Hello, welcome to the company!") # This is a method to greet the employee

SWS = employee()
SWS.salary = "900000" # This is an instance attribute and overrides the class atribute

SWS.greet()
SWS.getinfo() # This will print the instance attribute salary and class attribute language
