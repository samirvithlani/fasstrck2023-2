#param list ["naman","kumar","jain"]

def getPalindromes(names):
    return [i for i in names if i == i[::-1]]

# x = getPalindromes(["naman","kumar","jain","nitin","madam","radar","python"])
# print("x = ",x)


def validateName(names):
    newList=[]
    space = False
    for i in names:
        if " " not in i:
            newList.append(i)
    return newList       
            
    
        
        



data = ["nama n","kumar","amit thakkar","jatin patel","priya"]
x = validateName(data)
print("x = ",x)


