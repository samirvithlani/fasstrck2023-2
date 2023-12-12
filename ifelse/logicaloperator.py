#logical operators : and or not 

#cond 1 and cond 2

'''
    T   T   T
    F   -   F
    T   F   F

'''
#cond 1 and cond 2

'''
    T   -   T
    F   T   T
    F   F   F
'''

isHungry = True
havingMoneY = False

if isHungry and havingMoneY:
    print("Eat something")
else:
    print("Do not eat anything")    
