class programmer():
    company = "Google"
    def __init__(self, name, age):
        self.name = name
        self.age = age
       

    
p= programmer("Sarthak", 21)
print(p.name, p.age, p.company)  # This will print the instance attributes name
p= programmer("SWS", 22)
print(p.name, p.age, p.company)  # This will print the instance attributes name    


