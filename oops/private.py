class Test:
    
    def __init__(self):
        self.x = 10 # local variable
        self._no = 1000 # private variable
        self.__amount = 2000 # name mangling strong private variable
    
    def printMaount(self):
        print(self.__amount)
    
    


t = Test()
# print(t._no)
# print(t.__amount)        
# print(t.x)

t.printMaount()