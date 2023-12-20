#data = {} # empty dictionary
data = {1:"ram",2:"shyam",3:"mohan"} 
print(data)
print(type(data))

print(data[2])
print(data.get(2))

k = data.keys()
print("keys...",k)
v = data.values()
print("values...",v)


kv = data.items()
print("items...",kv)

for k,v in data.items():
    print(k,v)