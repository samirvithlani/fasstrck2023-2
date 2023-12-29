#single inheritance 1 - parent class  1 child class


class Bank:
    def __init__(self):
        self.balance = 0
        self.name = "RBI"
        self.rr = 4.5
    
    
    def repoRate(self):
        return self.rr
        
class SBI(Bank):
    
    def getRepoeRate(self):
        return self.repoRate()  
    
    def getBalance(self):
        return self.balance   



s = SBI()
print(s.getRepoeRate())
print(s.getBalance())  
print(s.repoRate())  