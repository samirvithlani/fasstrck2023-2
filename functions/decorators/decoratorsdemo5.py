def loginRequired(func):
    
    def inner(*args,**kwargs):
        
        if kwargs.get("userName") =="admin" and kwargs.get("password") =="admin":
            return func(*args,**kwargs)
    
    
    return inner



@loginRequired
def getData(*args,**kwargs):
    print(args)
    print(kwargs)
    print("You are able to access the data")    
    
    

getData(1,2,3,4,5,userName="admin",password="admin")    
    
    
    