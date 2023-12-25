#kwargss key word arguments

def getEmployeeData(x,**kwargs):
    print(x)
    print(kwargs)
   


getEmployeeData(100,name="Naman",age=20,city="Ahmedabad")    