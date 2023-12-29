class Shape:
    
    def __init__(self):
        self.length = 10
        self.breadth = 20
        print("Shape init")


class Triangle(Shape):
    
    def __init__(self):
        super().__init__()
        self.height = 30
        print("Triangle init")
        
    def area(self):
        print("Area of triangle...",self.length*self.height/2)


class Square(Shape):
    
    def __init__(self):
        super().__init__()
        self.side = 40
        print("Square init")
    
    def area(self):
        print("Area of square...",self.side*self.side)
        

s = Square()
s.area()

t = Triangle()
t.area()                    
        