def filterDict(data):
    return {k:v for k,v in data.items() if v > 1}


x = filterDict({"a":1,"b":2,"c":3,"d":4})
print("x = ",x)