name = "raj"
age = 20
email ="raj@gmail.com"
gender= "male"


file = open("./files/person.txt","a")
file.write("name = "+name+"\n")
file.write("age = "+str(age)+"\n")
file.write("email = "+email+"\n")
file.write("gender = "+gender+"\n")