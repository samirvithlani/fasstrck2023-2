lang = ["java", "python", "c", "c++", "python","c#"]
print(lang)

#removedelm = lang.pop() #pop withput index removes last element
# removedelm = lang.pop(2) 
# print("removing...",removedelm)


#lang.remove("pythona")

# cnt = lang.count("pythona")
# print("cnt = ", cnt)

if lang.count("pythona") > 0:
    lang.remove("pythona")
else:
    print("pythona not found")    

print(lang)