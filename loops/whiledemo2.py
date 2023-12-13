no = int(input("Enter a number: "))  #111 ->3

# 111 /10 -> 11 //10 -> 1 //10 -> 0
count =0
while no>0:
    no = no // 10
    count+=1

print("Total digits are: ",count)    

