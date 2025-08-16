class employee:
    salary = 100000 #THis is a class attribute
    lamguage = "Python"

SWS = employee()
SWS.name = "SWS" # This is an object attribute
print(SWS.name,SWS.salary, SWS.lamguage)

Sarthak = employee()
Sarthak.name = "Sarthak"
Sarthak.salary = 200000
Sarthak.lamguage = "Java"
print(Sarthak.name, Sarthak.salary, Sarthak.lamguage)