import re
position = [[] for i in range(9)]

f = open("Day 5 start.txt", "r")
for line in f:
    line = line.replace("\n", "")
    curRow = line[1::4]
    for i in range(len(curRow)):
        if curRow[i] != " ":
            position[i] = [curRow[i]] + position[i]

moves = []
f = open("Day 5 moves.txt")
for line in f:
    line = line.replace("\n", "")
    line = line[5:]
    temp = re.split(" from | to ", line)
    temp = [int(i) for i in temp]
    moves.append(temp)


def moveBlock(pos, start, end):
    pos[end].append(pos[start].pop())
    return pos

for i in moves:
    for j in range(i[0]):
        position = moveBlock(position, i[1] - 1, i[2] - 1)

print("".join([i.pop() for i in position]))

#Part 2
position = [[] for i in range(9)]

f = open("Day 5 start.txt", "r")
for line in f:
    line = line.replace("\n", "")
    curRow = line[1::4]
    for i in range(len(curRow)):
        if curRow[i] != " ":
            position[i] = [curRow[i]] + position[i]



def moveBlocks(pos, count, start, end):
    temp = []
    for block in range(count):
        temp.append(pos[start].pop())
    temp = temp[::-1]

    for block in temp:
        pos[end].append(block)
    return pos

for i in moves:
    position = moveBlocks(position, i[0], i[1] - 1, i[2] - 1)
print("".join([i.pop() for i in position]))