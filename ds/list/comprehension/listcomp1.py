data = [11,22,32,45,43,23,12]

evneList =[]
oddList = []


for i in data:
    if i % 2 == 0:
        evneList.append(i)
    else:
        oddList.append(i)


print("Even List: ",evneList)
print("Odd List: ",oddList)            



#[1,2,3,4,5,6,7,8,9,10]

# for i in range(1,11):
#    if i % 2 == 0:
#        x.append(i)


#x = [i for i in range(1,11)]
x = [i for i in range(1,15) if i %2 ==0]
print(x)