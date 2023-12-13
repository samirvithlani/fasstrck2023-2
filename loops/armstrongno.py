# 153 --> 1^3 + 5^3 + 3^3 = 153
no = int(input("Enter a number: "))  

rem =0
sum =0
while no >0:
    rem = no % 10 #153 --> 3 5 1
    sum = sum + rem ** 4 # 0 = 0 + 27 = sum = 27, 27 = 27 + 125 =152, 152 = 152 + 1 = 153
    no = no // 10 #153 --> 15
    

print("Sum of cube of digits is: ",sum)    
    
    