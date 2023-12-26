def smartDiv(func):
    
    def inner(a,b): #10 ,0 
        if b ==0:
            print("Cannot divide by zero")
        else:
            func(a,b)    
    
    return inner


@smartDiv
def division(a,b):
    print(a/b)
    

division (10,2)   
        