'''
    entry control loop  for while
        for:when we know the number of iterations
        
        for(int i=1i<11;i++){}
    
    while:
        when we dont know the number of iterations
        
    
    exit control loop : do while #no....
    
    range()
    range()
    range()
    
    membership operator: in, not in
'''
#range(10) #0-9
#range(1,11) #1-10
#range(1,11,2) #1,3,5,7,9
# for i in range(10):

# for i in range(1,20,2):
#     print(i,end=",")


for i in range(10,0,-1):
    print(i,end=",")
    
no = int(input("Enter a number: "))
   
for i in range(1,11):
    print(no ," * ",i," = ",no*i)    