class twodirectional:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x}x + {self.y}y")

class threedirectional:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        print(f"{self.x}x + {self.y}y + {self.z}z")    


o= twodirectional(1,2)
o.show()
p = threedirectional(1,2,3)
p.show() 

        
