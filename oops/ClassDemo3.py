class Users:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def getUsersData(self):
        print("self.name-->",self.name)
        print("self.age-->",self.age)


u =Users("John", 30)  
u.getUsersData()    
u1 = Users("Smith", 40)
u1.getUsersData()      