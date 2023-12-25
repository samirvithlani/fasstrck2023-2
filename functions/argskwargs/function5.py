#keyword arguments..
def getUserData(age,name,email,):
    print("Age: ",age)
    print("Name: ",name)
    print("Email: ",email)



#getUserData("Naman","naman@gmail.com")    
#getUserData("naman@gmail.com","Naman")    


#getUserData(email="naman@gmail.com",name="Naman",20) #compile time error
#getUserData(23,email="naman@gmail.com",name="Naman") #compile time error
getUserData(23,email="naman@gmail.com",name="Naman") #compile time error
