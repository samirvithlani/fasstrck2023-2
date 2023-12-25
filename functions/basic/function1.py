def test():
    print("without return without parameter")

test()    

def add(a,b):
    c = a + b
    print("sum = ",c)
    print("without return with parameter")


add(100,20)    


def mul(a,b,c):
    return a*b*c  // 3


def div():
    x = 10
    y = 20
    return x/y



ans = mul(10,20,30)
print("mul = ",ans)


print("div = ",div())


    