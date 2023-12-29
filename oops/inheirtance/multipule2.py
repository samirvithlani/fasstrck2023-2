class India:
    
    
    area = 1000
    def __init__(self):
        self.population = 100
        
        print("India is great")


class Russia:
    
    water = 2000
    def __init__(self):
        self.population = 200
        
        print("Russia")        


class Weapons(India,Russia):
    
    def __init__(self):
        super().__init__()
        print("Weapons init")

    
    def getWeapons(self):
        print("population...",self.population)
        print("area",India.area)
        # print("area...",self.area)
        # print("water...",self.water)
        


w = Weapons()
w.getWeapons()        
            
    
    