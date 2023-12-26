def outer(x,y):
    
    def inner():
        no1 = 100
        print("Inner function")
        print(x+y)

    print("Outer function")
    #print(no1)#Error
    inner()
    

outer(10,20)
