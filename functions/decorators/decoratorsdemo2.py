def isValid(func):
    age = 1
    def inner():
        if age >= 18:
            func()
        else:
            print("Not eligible")
    
    return inner


@isValid
def vote():
    print("You are eligible to vote")        
    

vote()    
    
            