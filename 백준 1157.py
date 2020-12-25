import sys

input = list(sys.stdin.readline())

myString = "".join(input)
myString = myString.replace('\n', "")
myString = myString.upper()

myDic = {}
i = 0

while(myString != ""):
    myDic[myString[0]] = myString.count(myString[0])
    myString = myString.replace(myString[0], "")
    i += 1

numCount = myDic.values()
m = max(numCount)

t = 0
for i in numCount:
    if i == m:
        t += 1

if t == 1:
    for key, value in myDic.items():
        if m == value:
            print(key)
            break
else: print('?')




