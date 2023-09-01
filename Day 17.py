f = open("Day 17 input.txt", "r")
global moves
moves = f.readlines()[0]
global moveIndex
moveIndex = 0

def removeEmptyTopLayers(board):
    lastEmptyRow = -1
    for i in range(len(board)):
        if board[i] == ".......":
            lastEmptyRow = i

    if lastEmptyRow != -1:
        del board[:lastEmptyRow + 1]
    return board

def allClearLeft(board, rockLocations, relevantRocks):
    for i in relevantRocks:
        rock = rockLocations[i]
        if rock[1] == 0:
            return False
        elif board[rock[0]][rock[1] - 1] == "#":
            return False
    return True

def allClearRight(board, rockLocations, relevantRocks):
    for i in relevantRocks:
        rock = rockLocations[i]
        if rock[1] == 6:
            return False
        elif board[rock[0]][rock[1] + 1] == "#":
            return False
    return True

def allClearDown(board, rockLocations, relevantRocks):
    for i in relevantRocks:
        rock = rockLocations[i]
        if board[rock[0] + 1][rock[1]] == "#":
            return False
    return True

def moveLeft(board, rockLocations):
    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "." + board[rock[0]][rock[1] + 1:]

    for r in range(len(rockLocations)):
        rockLocations[r] = [rockLocations[r][0], rockLocations[r][1] - 1]

    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "#" + board[rock[0]][rock[1] + 1:]

    return board, rockLocations

def moveRight(board, rockLocations):
    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "." + board[rock[0]][rock[1] + 1:]

    for r in range(len(rockLocations)):
        rockLocations[r] = [rockLocations[r][0], rockLocations[r][1] + 1]

    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "#" + board[rock[0]][rock[1] + 1:]

    return board, rockLocations

def moveDown(board, rockLocations):
    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "." + board[rock[0]][rock[1] + 1:]

    for r in range(len(rockLocations)):
        rockLocations[r] = [rockLocations[r][0] + 1, rockLocations[r][1]]

    for rock in rockLocations:
        board[rock[0]] = board[rock[0]][:rock[1]] + "#" + board[rock[0]][rock[1] + 1:]

    return board, rockLocations

def dropRock(board, rock):
    global moves
    global moveIndex
    rockLocationsDict = {0: [[0, 2], [0, 3], [0, 4], [0, 5]], 1: [[0, 3], [1, 2], [1, 3], [1, 4], [2, 3]],
                     2: [[0, 4], [1, 4], [2, 2], [2, 3], [2, 4]], 3: [[0, 2], [1, 2], [2, 2], [3, 2]],
                     4: [[0, 2], [0, 3], [1, 2], [1, 3]]}

    heightOfObject = {0:1, 1:3, 2:3, 3:4, 4:2}

    rocksWithNoRocksUnderneath = {0: [0, 1, 2, 3], 1: [1, 3, 4], 2: [2, 3, 4], 3: [3], 4: [2, 3]}
    rocksWithNoRocksOnLeft = {0: [0], 1: [0, 1, 4], 2: [0, 1, 2], 3: [0, 1, 2, 3], 4: [0, 2]}
    rocksWithNoRocksOnRight = {0: [3], 1: [0, 3, 4], 2: [0, 1, 4], 3: [0, 1, 2, 3], 4: [1, 3]}

    board = removeEmptyTopLayers(board)
    board = ["......." for i in range(3 + heightOfObject[rock])] + board
    rockLocations = rockLocationsDict[rock]

    for i in rockLocations:
        board[i[0]] = board[i[0]][:i[1]] + "#" + board[i[0]][i[1] + 1:]
    
    while(True):
        if moves[moveIndex] == "<": #Move left
            if allClearLeft(board, rockLocations, rocksWithNoRocksOnLeft[rock]):
                board, rockLocations = moveLeft(board, rockLocations)
        else: #Move Right
            if allClearRight(board, rockLocations, rocksWithNoRocksOnRight[rock]):
                board, rockLocations = moveRight(board, rockLocations)

        moveIndex += 1
        moveIndex = moveIndex % len(moves)
        if allClearDown(board, rockLocations, rocksWithNoRocksUnderneath[rock]):
            board, rockLocations = moveDown(board, rockLocations)
        else:
            return board

def display(board):
    for i in board:
        print(i)

def getHeight(board):
    height = 0
    for i in board:
        if "#" in i:
            height += 1
    return height - 1

board = ["#######"]
rocksToDrop = 2022
for i in range(rocksToDrop):
    board = dropRock(board, i % 5)

print(getHeight(board))
display(board)