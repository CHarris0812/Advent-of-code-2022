#Data is in the form (row, column)

terrain = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
startPos = ()
endPos = ()

counter = 0
f = open("Day 12 input.txt")
for line in f:
    temp = []
    line = line.replace("\n", "")

    for char in range(len(line)):
        if line[char] == "S":
            startPos = (counter, char)
            temp.append(0)
        elif line[char] == "E":
            endPos = (counter, char)
            temp.append(25)
        else:
            temp.append(alphabet.index(line[char]))

    counter += 1
    terrain.append([i for i in temp])


timesToHike = []

def findShortestPath(startLocation, endLocation):
    stepsToLocations = [[10000 for j in i] for i in terrain]

    toVisit = [(0, startLocation)]
    while len(toVisit) > 0:
        temp = toVisit.pop(0)
        stepsToGetHere = temp[0]
        currentLocation = temp[1]
        if stepsToGetHere < stepsToLocations[currentLocation[0]][currentLocation[1]]:
            stepsToLocations[currentLocation[0]][currentLocation[1]] = stepsToGetHere

            if endLocation == (currentLocation[0], currentLocation[1]):
                return stepsToGetHere

            currentValue = terrain[currentLocation[0]][currentLocation[1]]
                
            if len(terrain) > currentLocation[0] + 1:
                if terrain[currentLocation[0] + 1][currentLocation[1]] - currentValue <= 1:
                    if stepsToLocations[currentLocation[0] + 1][currentLocation[1]] > stepsToGetHere + 1:
                        toVisit.append((stepsToGetHere + 1, (currentLocation[0] + 1, currentLocation[1])))

            if currentLocation[0] > 0: 
                if terrain[currentLocation[0] - 1][currentLocation[1]] - currentValue <= 1:
                    if stepsToLocations[currentLocation[0] - 1][currentLocation[1]] > stepsToGetHere + 1:
                        toVisit.append((stepsToGetHere + 1, (currentLocation[0] - 1, currentLocation[1])))

            if len(terrain[0]) > currentLocation[1] + 1:
                if terrain[currentLocation[0]][currentLocation[1] + 1] - currentValue <= 1:
                    if stepsToLocations[currentLocation[0]][currentLocation[1] + 1] > stepsToGetHere + 1:
                        toVisit.append((stepsToGetHere + 1, (currentLocation[0], currentLocation[1] + 1)))

            if currentLocation[1] > 0:
                if terrain[currentLocation[0]][currentLocation[1] - 1] - currentValue <= 1:
                    if stepsToLocations[currentLocation[0]][currentLocation[1] - 1] > stepsToGetHere + 1:
                        toVisit.append((stepsToGetHere + 1, (currentLocation[0], currentLocation[1] - 1)))

        toVisit.sort()


for i in range(len(terrain)):
    for j in range(len(terrain[0])):
        if terrain[i][j] == 0:
            dist = findShortestPath((i, j), endPos)
            if dist != None:
                timesToHike.append(dist)

print(min(timesToHike))