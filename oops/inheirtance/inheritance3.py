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
        
    