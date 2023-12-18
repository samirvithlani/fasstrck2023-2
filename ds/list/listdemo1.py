users = ["raj", "ram", "ravi", "rakesh", "rajesh"]
#list iterable...
print("users = ", users)
print(type(users))

print("users 0 ", users[0])

users[0] = "RAJ"
print("users 0 ", users[0])


# for i in range(0,len(users)):
#     print(users[i])


for i in users:
    print(i)