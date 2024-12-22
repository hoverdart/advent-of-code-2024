file = open("text.txt", "r")
grid_list = [list(eachLine) for eachLine in file]
for y in range(len(grid_list)-1):
    grid_list[y].pop()
    for x in range(len(grid_list[y])):
        if grid_list[y][x] == "^":
            xCount = x
            yCount = y
            ogX = x
            ogY = y
            grid_list[yCount][xCount] = "X"
            break
count=0
xMax = len(grid_list[0])
yMax = len(grid_list)
currentDir = "up"
def moveInDir(y, x, grid):
    if currentDir == "up":
        if grid[y-1][x] != "#":
            return True
        else:
            return False
    elif currentDir == "down":
        if grid[y+1][x] != "#":
            return True
        else:
            return False
    elif currentDir == "left":
        if grid[y][x-1] != "#":
            return True
        else:
            return False
    elif currentDir == "right":
        if grid[y][x+1] != "#":
            return True
        else:
            return False
def move():
    if currentDir == "up": #yCount+=1
        return [-1, 0]
    elif currentDir == "down":
        return [1, 0]
    elif currentDir == "left":
        return [0, -1]
    elif currentDir == "right":
        return [0, 1]

def changeDir(currentDir):
    if currentDir == "up":
        return "right"
    elif currentDir == "down":
        return "left"
    elif currentDir == "left":
        return "up"
    elif currentDir == "right":
        return "down"

while xCount < xMax-1 and yCount < yMax-1 and xCount > 0 and yCount > 0:
    if moveInDir(yCount, xCount, grid_list):
        moving = move()
        yCount+=moving[0]
        xCount+=moving[1]
        grid_list[yCount][xCount] = "X"
    else:
        currentDir = changeDir(currentDir)

secondCt = 0
for y in range(len(grid_list)):
    for x in range(len(grid_list[y])):
        if grid_list[y][x] == "X":
            count+=1
            
            if y != ogY and x != ogX:
                filer = open("text.txt", "r")
                ogList = [list(eachLine) for eachLine in filer]
                for yy in range(len(ogList) - 1):
                    ogList[yy].pop()

                ogList[y][x] = "#"
                yCount = ogY
                xCount = ogX
                currentDir = "up"
                foolMeOnce = True
                SEEN = set()
                while True:
                    if (yCount, xCount, currentDir) in SEEN:
                        foolMeOnce = not foolMeOnce
                        if foolMeOnce:
                            secondCt += 1
                            break
                    SEEN.add((yCount, xCount, currentDir))
                    try:
                        if moveInDir(yCount, xCount, ogList):
                            moving = move()
                            yCount += moving[0]
                            xCount += moving[1]
                            ogList[yCount][xCount] = "X"
                        else:
                            currentDir = changeDir(currentDir)
                    except:
                        break
print(count)
print(secondCt)
