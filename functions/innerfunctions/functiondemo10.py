def outer(x,y):
    
    def inner():
        no1 = 100
        print("Inner function")
        return x+y

    print("Outer function")
    #print(no1)#Error
    ans = inner()
    print("sum  = ",ans)
    
    return ans * 2
    

ans = outer(10,20)
print("ans = ",ans)
