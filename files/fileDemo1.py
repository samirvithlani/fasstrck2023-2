file = open("./files/demo1.txt", "a") #if file is exist, it will be overwritten, if not, it will be created
file.write("Hello World\n")
file.close()
print("File created successfully")