class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print (f"the sqare is {self.n * self.n}")
    def cube(self):
        print (f"the sqare is {self.n * self.n * self.n}")
    def squareroot(self):
        print (f"the sqare is {self.n ** 0.5}")

a=calculator(4)
a.square()  # This will print the square of the number
a.cube()    # This will print the cube of the number
a.squareroot()  # This will print the square root of the number  