safeLists = 0
file = open("tooMuchText.txt", "r")
for eachLine in file:
  basicList = []
  flag=1
  basicList = eachLine.split()
  for num in range(0, len(basicList), 1):
    basicList[num] = int(basicList[num])
  ##Check if Increasing/Decreasing
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
      safeLists+=1
print(safeLists)
