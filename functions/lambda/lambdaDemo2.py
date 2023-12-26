#if else with lambda

#x = lambda a,b: a  if a >b else b
#print(x(10,20))

x = lambda a, b, c : a if a > b and a > c else b if b >c else c
print(x(10,20,30))


#for loop with lambda

