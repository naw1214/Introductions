# basic
for x in range(0,150):
    print(x)
# 5 to 1000 by 5
for x in range(5,1000,5):
    print(x)
# the dojo way
for x in range(1,100):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)
# that suckers huge
for x in range(0,500000):
    if x % 2 == 1:
        x += x
print(x)
# countdown by four
for x in range(2018,0,-4):
    print(x)
# flexible counter

lowNum = 2
highNum = 24
mult = 4

for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)