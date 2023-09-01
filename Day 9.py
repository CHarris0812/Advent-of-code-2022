moves = []
visited = []
headPos = [0, 0]
tailPos = [0, 0]
letterToMove = {"U":1, "R":1, "D":-1, "L":-1}
positions = [[0, 0] for i in range(10)]

f = open("Day 9 input.txt")
for line in f:
    moves.append([line[0], int(line[2:len(line)])])

def moveKnot (headPos, tailPos):
    tailDist = [tailPos[0] - headPos[0], tailPos[1] - headPos[1]]
    if abs(tailDist[0]) > 1 and tailDist[1] == 0: #Move left or right
        tailPos[0] += tailDist[0] // -2
    if abs(tailDist[1]) > 1 and tailDist[0] == 0: #Move up or down
        tailPos[1] += tailDist[1] // -2

    if (tailDist[0] > 1 and tailDist[1] >= 1) or (tailDist[0] >= 1 and tailDist[1] > 1): #Down and left
        tailPos[0] -= 1
        tailPos[1] -= 1

    if (tailDist[0] < -1 and tailDist[1] <= -1) or (tailDist[0] <= -1 and tailDist[1] < -1): #Up and right
        tailPos[0] += 1
        tailPos[1] += 1

    if (tailDist[0] > 1 and tailDist[1] <= -1) or (tailDist[0] >= 1 and tailDist[1] < -1): #Up and left
        tailPos[0] -= 1
        tailPos[1] += 1

    if (tailDist[0] < -1 and tailDist[1] >= 1) or (tailDist[0] <= -1 and tailDist[1] > 1): #Down and right
        tailPos[0] += 1
        tailPos[1] -= 1

    return tailPos

for move in moves:
    #print(move)
    for i in range(move[1]):        
        
        if move[0] in ["U", "D"]:
            positions[0][1] += letterToMove[move[0]]
        else:
            positions[0][0] += letterToMove[move[0]]

        for j in range(1, len(positions)):
            positions[j] = moveKnot(positions[j - 1], positions[j])
        
        visited.append((positions[-1][0], positions[-1][1]))
    #print(positions)    
        


    

print(len(set(visited)))