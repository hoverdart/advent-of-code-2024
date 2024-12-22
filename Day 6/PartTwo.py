file = open("text.txt", "r")
grid_list = [list(eachLine) for eachLine in file]
for y in range(len(grid_list)-1):
    grid_list[y].pop()
    for x in range(len(grid_list[y])):
        if grid_list[y][x] == "^":
            ogX, ogY = x,y
            ##grid_list[y][x] = "X"
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

secondCt = 0
for y in range(yMax):
    for x in range(xMax):
        xCount,yCount = ogX, ogY
        currentDir = "up"
        repeatedLoop = set() ##part 2
        finallyOver = set() ##part 1`
        while True:
            if (xCount, yCount, currentDir) in repeatedLoop:
                secondCt+=1
                break
            repeatedLoop.add((xCount, yCount, currentDir))
            finallyOver.add((xCount, yCount))
            moving = move()
            dy = yCount + moving[0]
            dx = xCount + moving[1]
            if not (0<=dy<yMax and 0<=dx<xMax):
                if(grid_list[y][x] == "#"):
                    count = len(finallyOver)
                break
            if grid_list[dy][dx] == "#" or dy == y and dx == x:
                currentDir = changeDir(currentDir)
            else:
                yCount= dy
                xCount = dx
print(count) #Part 1
print(secondCt) #Part 2
