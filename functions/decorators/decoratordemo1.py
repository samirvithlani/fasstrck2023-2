
#func --> throwParty
def orderFood(func):
    
    def inner():
        print("Ordering food")
        func()
    
    return inner    


@orderFood
def throwParty():
    print("Throwing a party")
    


throwParty()
#orderFood(throwParty())