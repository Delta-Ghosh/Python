class Employee:
    a = 1

    # def show(self):
    #     print (f"The Class artibute is {self.a}")

    @classmethod
    def show(cls):
        print (f"The Class attribute is {cls.a}")

e= Employee()
e.a = 2
print(e.a) # This will print 2, as it is an instance attribute
Employee.show() # This will print the class attribute