class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, num): # Overloading the + operator 
        return self.n + num.n # num is an instance of number

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))

print(n + m)  # This will raise an error since __add__ is not defined