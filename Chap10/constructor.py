class employee:
    salary = 100000 #THis is a class attribute
    lamguage = "Python"

    def __init__(self): #dunder method to initialize the object
        print("Employee object created.") #print a message when an object is created

SWS = employee()
SWS.name = "SWS" # This is an object attribute
print(SWS.name,SWS.salary, SWS.lamguage)

Sarthak = employee()
Sarthak.name = "Sarthak"
Sarthak.salary = 200000
Sarthak.lamguage = "Java"
print(Sarthak.name, Sarthak.salary, Sarthak.lamguage)