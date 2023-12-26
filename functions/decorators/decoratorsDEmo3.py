def isManager(func):
    
    def inner(flag):
        print("flag",flag)
        if flag == "manager":
            func()
        else:
            print("You are not a manager")
    
    return inner

@isManager
def getData():
    print("You are a manager and able to access the data")             
    

getData("manager")    