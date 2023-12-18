lang = ["java", "python", "c", "c++", "c#"]
print(lang)
lang.append("php")
print(lang)

lang.extend(["ruby", "perl"])
lang.extend("OK")
print(lang)

lang.insert(1,"scala")
lang.insert(3,["go", "rust"])
print(lang)
