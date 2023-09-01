rocks = []
f = open("Day 14 input.txt")
drop = [0, 500]
maxY = 0

for line in f:
    line = line.replace("\n", "")
    temp = line.split(" -> ")
    curRocks = []

    for j in temp:
        i = j.split(",")
        i = [int(i[1]), int(i[0])]

        curRocks.append([k for k in i])

        if int(i[0]) > maxY:
            maxY = int(i[0])
    rocks.append([r for r in curRocks])

maxY += 2
rocks.append([[maxY, 0], [maxY, 999]])
terrain = [["." for j in range(1000)] for i in range(maxY + 1)]

def drawLine(start, end, terrain):
    if start[0] == end[0]: #Vertical
        for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            terrain[start[0]][i] = "#"
    else:
        for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            terrain[i][start[1]] = "#"
    return terrain

for i in rocks:
    for j in range(len(i) - 1):
        terrain = drawLine(i[j], i[j + 1], terrain)

#Good at this point

def dropSand(drop, terrain, bottom):
    curPos = [i for i in drop]
    while True:
        if terrain[curPos[0] + 1][curPos[1]] == ".":
            curPos[0] += 1
        elif terrain[curPos[0] + 1][curPos[1] - 1] == ".":
            curPos[0] += 1
            curPos[1] -= 1
        elif terrain[curPos[0] + 1][curPos[1] + 1] == ".":
            curPos[0] += 1
            curPos[1] += 1
        else:
            if curPos[0] == 0 and curPos[1] == 500:
                return terrain, True
            terrain[curPos[0]][curPos[1]] = "O"
            return terrain, False


sandDropped = 0
while True:
    sandDropped += 1
    terrain, stopped = dropSand(drop, terrain, maxY)
    if stopped:
        print(sandDropped)
        break