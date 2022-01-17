from random import randint
import math

space = "    "

def start(width):
    center = width/2
    center = math.floor(center)
    return center

def getOppositeDirection(d):
    if d == 0: return 2
    if d == 1: return 3
    if d == 2: return 0
    if d == 3: return 1
def getNextDirection(x, y, gridPoints, width):
    for i in range(10):
        offset = [0,0,randint(0,3)]
        direction = offset[2]
        if direction == 0:
            offset[0] = 0
            offset[1] = -1

        if direction == 1:
            offset[0] = 1
            offset[1] = 0

        if direction == 2:
            offset[0] = 0
            offset[1] = 1

        if direction == 3:
            offset[0] = -1
            offset[1] = 0
        if x + offset[0] < 0 or x + offset[0] > width-1:
            return 0
        if y + offset[1] < 0 or y + offset[1] > width-1:
            return 0
        if gridPoints[x+offset[0]][y+offset[1]] == 0:
            return offset   
    return -1
def drawScreen(gridPoints, vertices ,center):
    highest = 0
    for y in range(width):
        for x in range(width):
            if gridPoints[x][y] > highest:
                highest = gridPoints[x][y]
                highestX=x+1
                highestY=y+1
    for y in range(width):
        hlineString = ""
        vlineString = ""
        for x in range(width):
            hsegment = ""
            vsegment = ""
            #if gridPoints[highestX-1][highestY-1] == 
                #gridPoints[highestX-1][highestY-1] = 11
                #gridPoints[center][center] = 11
            if gridPoints[x][y] > 0:
                if x+1 < width and vertices[x][y][1]:
                    hsegment = "==="
                else:
                    hsegment = "   "
                if y+1 < width and vertices[x][y][2]:
                    vsegment = "||   "
                else:
                    vsegment = "     "
            else:
                hsegment = "   "
                vsegment = "     "
            hlineString += str(gridPoints[x][y]).zfill(2)+hsegment
            vlineString += vsegment
        print(hlineString)
        print(vlineString)

def makeMaze(startX, startY, width, minComplexity, backtrackStack, gridPoints, vertices):
    
    x = startX
    y = startY
    if gridPoints[x][y] == 0:
        number = 1
    else:
        number = gridPoints[x][y]

    gridPoints[x][y] = number
    number += 1
    ok = True
    while ok == True:
        nextStep = getNextDirection(x,y,gridPoints,width)
        if nextStep == 0 and number >= minComplexity:
            return True
        if nextStep == 0 and number < minComplexity:
            return False
        if nextStep == -1:
            return False
        lastX = x
        lastY = y
        x += nextStep[0]
        y += nextStep[1]
        
        if x < 0 or x > width:
            break
        if y < 0 or y > width:
            break
        gridPoints[x][y] = number
        
        vertices[lastX][lastY][nextStep[2]] = True
        vertices[x][y][getOppositeDirection(nextStep[2])] = True
        backtrackStack.append([x, y, number])
        number += 1
    return True

width=13
minComplexity = 70
start=start(width)
success = False

while not success:
    backtrackStack = []
    gridPoints=[[00] * width for i in range(width)]
    vertices=[[[False for j in range(4)] for i in range(width)] for i in range(width)]
    success = makeMaze(start, start, width, minComplexity, backtrackStack, gridPoints, vertices)

substacks = []
for newStart in backtrackStack:
    subStack = []
    makeMaze(newStart[0], newStart[1], width, 1, subStack, gridPoints, vertices)
    substacks.append(subStack)

for stack in substacks:
    for newStart in stack:
        subStack = []
        makeMaze(newStart[0], newStart[1], width, 1, subStack, gridPoints, vertices)


drawScreen(gridPoints, vertices, start)
