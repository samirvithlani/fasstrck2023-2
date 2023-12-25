# def getUsers(users):
#     print(users)


# getUsers("raj")    
# getUsers("raj","naman")

def getUsers(*args):
    print(args)
    print(type(args))
    


# getUsers() 
# getUsers("raj")
# getUsers("raj","naman")
# getUsers("raj","naman","jatin")   


def studentData(*args,x):
    print(args)
    print(x)


studentData("raj","naman",x=100)    