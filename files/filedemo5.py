file = open("./files/person.txt","r")

data = file.readlines()

for line in data:
    print(line,end="")