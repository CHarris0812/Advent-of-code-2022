board = []
f = open("Day 8 input.txt", "r")
for line in f:
    line = line.replace("\n", "")
    board.append([int(char) for char in line])


visibleFromLeft = [[False for i in range(len(board[0]))] for j in range(len(board))]
visibleFromRight = [[False for i in range(len(board[0]))] for j in range(len(board))]
visibleFromTop = [[False for i in range(len(board[0]))] for j in range(len(board))]
visibleFromBottom = [[False for i in range(len(board[0]))] for j in range(len(board))]
visible = [[0 for i in range(len(board[0]))] for j in range(len(board))]

for i in range(len(board)):
    visibleFromLeft[i][0] = True
    for j in range(1, len(board[0])):
        if board[i][j] > max([board[i][k] for k in range(j)]):
            visibleFromLeft[i][j] = True

for i in range(len(board)):
    visibleFromRight[i][-1] = True
    for j in range(len(board[0]) - 2, -1, -1):
        if board[i][j] > max([board[i][k] for k in range(j + 1, len(board[0]))]):
            visibleFromRight[i][j] = True

visibleFromTop[0] = [True for i in range(len(board[0]))]
for i in range(1, len(board)):
    for j in range(len(board[0])):
        if board[i][j] > max([board[k][j] for k in range(i)]):
            visibleFromTop[i][j] = True

visibleFromBottom[-1] = [True for i in range(len(board[0]))]
for i in range(len(board) - 2, -1, -1):
    for j in range(len(board[0])):
        if board[i][j] > max([board[k][j] for k in range(i + 1, len(board))]):
            visibleFromBottom[i][j] = True

for i in range(len(board)):
    for j in range(len(board[0])):
        if visibleFromLeft[i][j] or visibleFromRight[i][j] or visibleFromTop[i][j] or visibleFromBottom[i][j]:
            visible[i][j] = 1

print(sum([sum(i) for i in visible]))


def visibleFromSpot(row, col):
    return visibleToLeft(row, col) * visibleToRight(row, col) * visibleToTop(row, col) * visibleToBottom(row, col)

def visibleToLeft(row, col):
    global board
    height = board[row][col]
    i = col - 1
    visible = 0
    while i >= 0:
        visible += 1
        if board[row][i] >= height:
            break
        i -= 1
    return visible

def visibleToRight(row, col):
    global board
    height = board[row][col]
    i = col + 1
    visible = 0
    while i < len(board[0]):
        visible += 1
        if board[row][i] >= height:
            break
        i += 1
    return visible

def visibleToTop(row, col):
    global board
    height = board[row][col]
    i = row - 1
    visible = 0
    while i >= 0:
        visible += 1
        if board[i][col] >= height:
            break
        i -= 1
    return visible

def visibleToBottom(row, col):
    global board
    height = board[row][col]
    i = row + 1
    visible = 0
    while i < len(board):
        visible += 1
        if board[i][col] >= height:
            break
        i += 1
    return visible

visible = [[-1 for i in board[0]] for j in board]

for i in range(len(board)):
    for j in range(len(board)):
        visible[i][j] = visibleFromSpot(i, j)

print(max([max(i) for i in visible]))