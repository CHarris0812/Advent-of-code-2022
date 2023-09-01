lava = [[[0 for i in range(20)] for j in range(20)] for k in range(20)]
reachable = [[[False for i in range(20)] for j in range(20)] for k in range(20)]

f = open("Day 18 input.txt", "r")
for line in f:
    line = line.replace("\n", "")
    coords = line.split(",")
    coords = [int(i) for i in coords]
    lava[coords[0]][coords[1]][coords[2]] = 1


def countAdjacents (lava, x, y, z):
    adjacents = 0
    
    for i in [-1, 1]:
        if x + i >= 0 and x + i <= 19:
            if lava[x + i][y][z] == 1:
                adjacents += 1

    for i in [-1, 1]:
        if y + i >= 0 and y + i <= 19:
            if lava[x][y + i][z] == 1:
                adjacents += 1

    for i in [-1, 1]:
        if z + i >= 0 and z + i <= 19:
            if lava[x][y][z + i] == 1:
                adjacents += 1
    return adjacents

surfaceArea = 0

for i in range(20):
    for j in range(20):
        for k in range(20):
            if lava[i][j][k] == 1:
                surfaceArea += 6 - countAdjacents(lava, i, j, k)

print(surfaceArea)

reachables = []

#Part 2
for i in range(20):
    for j in range(20):
        for k in range(20):
            if i == 0 or i == 19 or j == 0 or j == 19 or k == 0 or k == 19:
                #reachable[i][j][k] = True
                reachables.append([i, j, k])

def getAdjacents(x, y, z):
    adjacents = []
    if x > 0:
        adjacents.append([x - 1, y, z])
    if x < 19:
        adjacents.append([x + 1, y, z])
    if y > 0:
        adjacents.append([x, y - 1, z])
    if y < 19:
        adjacents.append([x, y + 1, z])
    if z > 0:
        adjacents.append([x, y, z - 1])
    if z < 19:
        adjacents.append([x, y, z + 1])
    return adjacents


while len(reachables) > 0:
    current = reachables.pop(0)
    if reachable[current[0]][current[1]][current[2]] == False:
        reachable[current[0]][current[1]][current[2]] = True

        if lava[current[0]][current[1]][current[2]] == 0:
            reachables += getAdjacents(current[0], current[1], current[2])


for i in range(20):
    for j in range(20):
        for k in range(20):
            if not reachable[i][j][k]:
                lava[i][j][k] = 1
                
surfaceArea = 0

for i in range(20):
    for j in range(20):
        for k in range(20):
            if lava[i][j][k] == 1:
                surfaceArea += 6 - countAdjacents(lava, i, j, k)

print(surfaceArea)
print(reachable[2][2])