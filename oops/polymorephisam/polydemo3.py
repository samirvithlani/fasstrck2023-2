from multipledispatch import dispatch


class Calc:
    
    @dispatch(int, int)
    def add(self, a, b):
        print("int add")
        return a + b
    
    @dispatch(int, int, int)
    def add(self, a, b, c):
        print("int add with 3 params")
        return a + b + c
    
    @dispatch(float, float)
    def add(self,a,b):
        print("float add")
        return a+b

c = Calc()
c.add(10,20,10)
    




    