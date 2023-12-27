class Uni:
    
    name = "GTU" #class variable / static variable
    
    def getUniData(self):
        self.collage = "LJ" #Instance variable
        print("Uni.name-->",Uni.name) #access in a static way
        


u = Uni()     
u.getUniData() #access in a static way
print("UNI name-->",Uni.name) #access in a static wayp
print("u.collage-->",u.collage) #access in a static way
print(Uni.collage)