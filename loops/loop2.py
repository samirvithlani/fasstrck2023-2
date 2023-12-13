no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))

sum =0
for i in range(no1,no2+1):
    if i % 3 == 0 and i % 4==0:
        sum = sum + i
        print(i,end=",")

print("Sum is: ",sum)        
    