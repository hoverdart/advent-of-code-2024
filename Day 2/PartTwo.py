safeLists = 0
allLists = []
file = open("tooMuchText.txt", "r")
for eachLine in file:
  basicList = []
  basicList = eachLine.split()
  for num in range(0, len(basicList), 1):
    basicList[num] = int(basicList[num])
  allLists.append(basicList)
def checkSafety(basicList):
  ##Check if Increasing/Decreasing
  flag=1
  testList = basicList.copy()
  testList.sort()
  if basicList == testList:
    flag=0
  testList.sort(reverse=True)
  if basicList == testList:
    flag=0
  ##Greater than 1, less than 3
  if flag==0:
    basicList.sort()
    for num in range(0, len(basicList)-1, 1):
      if basicList[num+1] - basicList[num] < 1 or basicList[num+1] - basicList[num] > 3:
        flag=1
    if flag==0:
      return True
    else:
      return False
for oneList in allLists:
  if checkSafety(oneList):
    safeLists+=1
  else:
    for n in range(0, len(oneList), 1):
      newList = oneList.copy()
      newList.pop(n)
      if checkSafety(newList):
        safeLists+=1
        break
print(safeLists)
