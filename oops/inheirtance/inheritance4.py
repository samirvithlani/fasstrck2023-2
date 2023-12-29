class Gov:
    
    def __init__(self):
        self.party = "BJP"
        self.pm = "Narendra Modi"
        self.fund = 100


class State(Gov):
    
    def __init__(self):
        super().__init__()
        self.stateName = "Gujarat"
        self.cm = "Bhupendra Patel"
        self.grant = 1000
    
    
    def getGovDetail(self):
        print("gov party...",self.party)    
        print("gov pm...",self.pm)
        print("gov fund...",self.fund)
        
            
class AMC(State):
    
    def __init__(self):
        from Inheritance2 import Gov

class State(Gov):
    
    def __init__(self):
        self.stateName = "Gujarat"
        self.cm = "Bhupendra Patel"
        self.grant = 1000
    
    
    def getGovDetail(self):
        print("gov party...",self.party)    
        print("gov pm...",self.pm)
        print("gov fund...",self.fund)
        
    
        self.amcName = "AUDA"
        self.tax =5000
    
    
    def getAllDetails(self):
        
        print("Gov Details...")
        print("gov party...",self.party)
        print("gov pm...",self.pm)
        print("gov fund...",self.fund)
        print("State Details...")
        print("state name...",self.stateName)
        print("state cm...",self.cm)
        print("state grant...",self.grant)
        print("AMC Details...")
        print("amc name...",self.amcName)
        print("amc tax...",self.tax)
        
            

s = State()
s.getGovDetail()