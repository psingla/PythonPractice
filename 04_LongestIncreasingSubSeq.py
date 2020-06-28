mylist = [4,5,3,9,10,3,4,5,7,20,13,10,11,15,29]
#mylist = [10,3,5,6]
currentcnt = 0
longestcnt = 0
currentStartIndex = 0
CurrentEndIndex = 0
longStartIndex = 0
longEndIndex = len(mylist)

""""
for i in range(0,len(mylist)-1):
    print(i)
    print(mylist[i])
"""


for i in range(0,len(mylist)-1):
    currentcnt += 1
    CurrentEndIndex += 1
    if mylist[i] > mylist[i+1] or i == len(mylist)-2:
        if longestcnt < currentcnt:
            longStartIndex = currentStartIndex
            longEndIndex = CurrentEndIndex
            currentStartIndex = i+1
            CurrentEndIndex = currentStartIndex
            longestcnt = currentcnt
            currentcnt = 0

print (longStartIndex)
print (longEndIndex)

for i in range(longStartIndex,longEndIndex+1):
    print(mylist[i])







