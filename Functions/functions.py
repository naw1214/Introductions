# Countdowns
def countdown(num):
    newList = []
    for x in range(num,0,-1):
        newList.append(x)
    return newList
print(countdown(5))
#Print and Return
def prntRtrn(list):
    print(list[0])
    return list[1]
print(prntRtrn([33,12]))
# sum and length
def sumLngth(list):
    sum = list[0] + len(list)
    return sum
sumLngth([1,2,3,4,5])
# list greater than 2nd val
def listComp(list):
    newList = []
    count = 0
    if(len(list)<=2):
        return 'List not big enough'
    for x in range(list[0],len(list)):
        if(list[x] > list[1]):
            newList.append(list[x])
    return newList, len(newList)
listComp([2,3,13,22])
# this length that value
def lenVal(length, value):
    newList = []
    newList.append(value)
    newList *= length
    return newList
lenVal(4,5)

