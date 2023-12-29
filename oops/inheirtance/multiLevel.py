class A:
    
    def __init__(self):
        self.a = 10

class B(A):
    
    def __init__(self):
        super().__init__()
        self.b = 20        

    def detail(self):
        print("a...",self.a)
        print("b...",self.b)
        


class C(B):
    
    def __init__(self):
        print("C init")

    def detail(self):
        #print("a...",self.a)
        #print("b...",self.b)
        super().detail()        
        
b = B()
b.detail()        
        