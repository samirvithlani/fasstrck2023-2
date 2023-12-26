def getNames(names):
    return [i for i in names if len(i) > 5]



#x = lambda names : [i for i in names if len(i) > 5]
x = lambda names : getNames(names)

ans = x(["abc","abcd","abcde","abcdef","abcdefg","abcdefgh"])
print(ans)