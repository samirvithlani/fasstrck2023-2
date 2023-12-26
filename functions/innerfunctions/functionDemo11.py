def outer(x,y):
    
    def inner(p1,p2):
        no1 = 100
        print("Inner function")
        return x+y + p1 + p2

    return inner(10,20)    

ans = outer(10,20)
print("ans = ",ans)
