def getUsersToUpper(users):
    print("Users in upper case")
    print(users)
    print("type",type(users))
    
    return [i.upper() for i in users]
    
    



x = getUsersToUpper(["raj", "ram", "ravi","partik","naveen"])
print("x = ",x)

    