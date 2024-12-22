import time
file = open("text.txt", "r")
grid_list = [list(eachLine) for eachLine in file]
count=0
xMax = len(grid_list[0])
yMax = len(grid_list)
xCount = 0
yCount = 0
currentDir = "up"
def moveInDir(y, x):
    if currentDir == "up":
        if grid_list[y-1][x] != "#":
            return True
        else:
            return False
    elif currentDir == "down":
        if grid_list[y+1][x] != "#":
            return True
        else:
            return False
    elif currentDir == "left":
        if grid_list[y][x-1] != "#":
            return True
        else:
            return False
    elif currentDir == "right":
        if grid_list[y][x+1] != "#":
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
for y in range(len(grid_list)):
    grid_list[y].pop()
    for x in range(len(grid_list[y])):
        if grid_list[y][x] == "^":
            xCount = x
            yCount = y
            grid_list[yCount][xCount] = "X"
            break
while xCount < xMax-1 and yCount < yMax-1 and xCount > 0 and yCount > 0:
    if moveInDir(yCount, xCount):
        moving = move()
        yCount+=moving[0]
        xCount+=moving[1]
        grid_list[yCount][xCount] = "X"
    else:
        currentDir = changeDir(currentDir)
    time.sleep(0.5)
    for y in range(len(grid_list)):
        print(grid_list[y])
for y in range(len(grid_list)):
    for x in range(len(grid_list[y])):
        if grid_list[y][x] == "X":
            count+=1
print(count)
