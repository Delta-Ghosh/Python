class employee:
    salary = int(input("Enter the salary: "))
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary * self.increment/100) + self.salary
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = ((value - self.salary) * 100)/self.salary
e = employee()

print(e.increment)
print(e.salaryAfterIncrement)