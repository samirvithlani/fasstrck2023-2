emails =["s amir@gmail.com","amit@gmail.com","jan may@gmail.com"]

x = lambda email : [i for i in email if  " " not in i]
print(x(emails))



x1 = lambda *args : [i for i in args if i % 2 == 0]
print(x1(1,2,3,4,5,6,7,8,9,10))