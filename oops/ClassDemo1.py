class Vehilce:

    def getVehData(self): #v
        self.name = "BMW"  #instance variable
        name = "AUDI"#local variable
        print("This is a vehicle class")
        print("self",self)
        # print("name-->",name)
        # print("self.name-->",self.name)

    def printVehData(self): #v1
        print(self)
        print("self.name-->",self.name)



v = Vehilce()
v1 = Vehilce()
print("v",v)
v.getVehData() #error default class current object is pass... 
v1.printVehData()       
    