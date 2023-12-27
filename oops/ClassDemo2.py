class Car:
    
    
    def __init__(self):
        print("This is a constructor")
        self.name = "BMW" #instance variable
        self.color = "Black" #instance variable
    
    
    def printCarData(self):
        print("self.name-->",self.name)
        print("self.color-->",self.color)    
        
    


c = Car()        
c.name = "AUDI"
c.color = "White"
c.printCarData()

c1 = Car()
c1.printCarData()
        