class Test:
    
    IFSC = "SBIN0001234" #static variable
    #static method
    @staticmethod
    def myTest():
        
        print("This is myTest() method")
    
    @classmethod
    def myTest2(self):
        self.name = "surya"
        print("This is myTest2() method")    
        


Test.myTest()        


t = Test()
t.myTest2()
print(Test.IFSC)
print(t.name)
