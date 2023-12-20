data = {"java":["amit","raj","parth"],"python":["amit","parth","priya","kunal"]}

data["java"].append("mohan")
data["python"].remove("parth")

for k,v in data.items():
    print(k)
    
    for i in v:
        print(i)
    
    print("*************")    