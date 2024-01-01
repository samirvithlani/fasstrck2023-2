#read,readLine,readLines

name =""
age = 0
email =""
gender = ""

file = open("./files/person.txt","r")
#using read function
data = file.read()
#data = file.read(4)
print(data)
name = data[6:10]
email = data[22:32]
print("name = ",name)
