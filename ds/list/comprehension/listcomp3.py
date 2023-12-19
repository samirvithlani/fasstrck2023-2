lang = ["hindi","naman","malayalam","tamil","telugu"]
#palindromw -> list else  --> upper case

#x = [i for i in lang if i == i[::-1] else i.upper()]
#how to write else in list comprehension
x =[i if i == i[::-1] else i.upper() for i in lang]
print(x)

marks = [67,78,89,45,31,32,12]

#30 > and 35< +5 else as it is

x = [i+5 if i >30 and i<35 else i for i in marks]
print(x)

data = ["amit","sumit","ram","shyam","mohan","sohan","hr","jaya","geeta"]
# len>3 upper case else title case

x  = [i.upper() if len(i)>3 else i.title() for i in data]
print(x)

