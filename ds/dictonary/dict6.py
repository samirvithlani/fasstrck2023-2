#x = {i:i for i in range(1,11)}
x = {i:i for i in range(1,11) if i %2 ==0}

data =[100,20,30,405,60,70]

#x1 = {i:i for i in data}
#{1:100,2:20,3:30,4:405,5:60,6:70}



#x1 = {k:i for i in data for k in range(1,11)}
#x1  = {i + 1: data[i] for i in range(len(data))}
x1 = {i+1 : data[i] ** 2 if i  % 2 ==0 else data[i] **3 for i in range(len(data))}






print(x)
print(x1)