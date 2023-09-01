board = []
f = open("Day 24 input.txt", "r")

for line in f:
    line = line.replace("\n", "")
    board.append(line[1:-1])

board = board[1:]
board = board[:-1]


def makeBoard(minute):
    global board
    newBoard = [["." for j in range(len(board[0]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ">":
                newBoard[i][(j + minute) % len(board[0])] = "#"
            if board[i][j] == "<":
                newBoard[i][(j - minute) % len(board[0])] = "#"
            if board[i][j] == "v":
                newBoard[(i + minute) % len(board)][j] = "#"
            if board[i][j] == "^":
                newBoard[(i - minute) % len(board)][j] = "#"
    return newBoard

boards = []
lcm = len(board) * len(board[0])
for i in range(lcm):
    boards.append(makeBoard(i))

def availableSpots(pos, board):
    spots = []
    if board[pos[0]][pos[1]] == ".":
        spots.append((pos[0], pos[1]))
    if pos[0] > 0:
        if board[pos[0] - 1][pos[1]] == ".":
            spots.append((pos[0] - 1, pos[1]))
    if pos[0] < len(board) - 1:
        if board[pos[0] + 1][pos[1]] == ".":
            spots.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        if board[pos[0]][pos[1] - 1] == ".":
            spots.append((pos[0], pos[1] - 1))
    if pos[1] < len(board[0]) - 1:
        if board[pos[0]][pos[1] + 1] == ".":
            spots.append((pos[0], pos[1] + 1))
    return spots

position = (-1, 0) #Row, column
visited = [(0, position)]
timeToVisit = [[[10000000000 for k in board[0]] for j in board] for i in boards]
while len(visited) != 0:
    visited.sort()
    current = visited.pop(0)
    minute = current[0] + 1
    pos = current[1]
    if pos == (-1, 0) or timeToVisit[minute % lcm][pos[0]][pos[1]] > minute:
        if pos == (len(board) - 1, len(board[0]) - 1):
            print(minute)
            break
        if pos != (-1, 0):
            timeToVisit[minute % lcm][pos[0]][pos[1]] = minute
            spots = availableSpots(pos, boards[minute % lcm])
        else:
            spots = [(-1, 0)]
            if boards[minute % lcm][0][0] == ".":
                spots.append((0, 0))

        for s in spots:
            visited.append((minute, s))

position = (len(board), len(board[0]) - 1) #Row, column
visited = [(minute, position)]
timeToVisit = [[[10000000000 for k in board[0]] for j in board] for i in boards]
while len(visited) != 0:
    visited.sort()
    current = visited.pop(0)
    minute = current[0] + 1
    pos = current[1]
    if pos == position or timeToVisit[minute % lcm][pos[0]][pos[1]] > minute:
        if pos == (0, 0):
            print(minute)
            break
        if pos != position:
            timeToVisit[minute % lcm][pos[0]][pos[1]] = minute
            spots = availableSpots(pos, boards[minute % lcm])
        else:
            spots = [pos]
            if boards[minute % lcm][-1][-1] == ".":
                spots.append((len(board) - 1, len(board[0]) - 1))
        for s in spots:
            visited.append((minute, s))


position = (-1, 0) #Row, column
visited = [(minute, position)]
timeToVisit = [[[10000000000 for k in board[0]] for j in board] for i in boards]
while len(visited) != 0:
    visited.sort()
    current = visited.pop(0)
    minute = current[0] + 1
    pos = current[1]
    if pos == (-1, 0) or timeToVisit[minute % lcm][pos[0]][pos[1]] > minute:
        if pos == (len(board) - 1, len(board[0]) - 1):
            print(minute)
            break
        if pos != (-1, 0):
            timeToVisit[minute % lcm][pos[0]][pos[1]] = minute
            spots = availableSpots(pos, boards[minute % lcm])
        else:
            spots = [(-1, 0)]
            if boards[minute % lcm][0][0] == ".":
                spots.append((0, 0))

        for s in spots:
            visited.append((minute, s))
