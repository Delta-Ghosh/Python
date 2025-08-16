class employee:
    salary = 100000 #THis is a class attribute
    lamguage = "Python"

    def __init__(self, salary, lamguage):
        self.salary = 15000
        self.lamguage = "java" 
        print("Employee object created.")

# SWS = employee()
# SWS.name = "SWS" # This is an object attribute
# print(SWS.name,SWS.salary, SWS.lamguage)


sarthak = employee( "salary","lamguage")

print(sarthak.salary, sarthak.lamguage) # This will print the instance attributes salary and lamguage