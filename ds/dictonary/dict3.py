marks = {"maths": 90, "science": 80, "english": 70}

# removedElm = marks.pop("maths")
# print(removedElm)
# print(marks)


removedData = marks.popitem()
print(removedData)
print(marks)

#x = marks.fromkeys("maths",100)

x = dict.fromkeys(["amit","raj","parth"],100)

print(x)