with open("./files/person.txt","r") as file:
    
    while True:
        data = file.readline()
        print(data,end="")
        if data == "":
            break
        
        