no =123

rem = 0
sum = 0
while no>0:
    rem = no % 10  #3 #2 #1
    sum = sum * 10 + rem # sum = 0 * 10 + 3 = 3 # sum = 3 * 10 + 2 = 32 # sum = 32 * 10 + 1 = 321
    no = no // 10 
    

print("Reverse number is: ",sum)    

#palindrome....