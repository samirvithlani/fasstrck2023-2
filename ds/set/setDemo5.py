user1 = {"ram","shyam","priya"}
user2 = {"ram","shyam","sita"}

#x = user1.union(user2)
x = user1.difference(user2)
# x = user2.difference(user1)
#x = user1.intersection(user2)
#x = user1.symmetric_difference(user2)
#print(x)


#user1.difference_update(user2)
#print(user1)

x = user1.copy()
print(x)

#set comprehension

x = {i for i in range(1,11)}
print(x)
