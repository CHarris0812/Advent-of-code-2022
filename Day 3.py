firstSack = []
secondSack = []

f = open("Day 3 input.txt", "r")
for line in f:
    line = line[:len(line) - 1]
    firstSack.append(line[:len(line) // 2])
    secondSack.append(line[len(line) // 2:])



def getVal(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(letter) + 1

def findDuplicate(str1, str2):
    for i in range(len(str1)):
        if str1[i] in str2:
            return str1[i]

score = 0
for i in range(len(firstSack)):
    duplicateLetter = findDuplicate(firstSack[i], secondSack[i])
    score += getVal(duplicateLetter)

#print(score)

#Part 2
sacks = []
f = open("Day 3 input.txt", "r")
counter = 0
temp = []
for line in f:
    line = line[:len(line) - 1]
    if counter < 3:
        temp.append(line)
        counter += 1
    else:
        sacks.append([i for i in temp])
        temp = [line]
        counter = 1
sacks.append([i for i in temp])

def findTriple(sack1, sack2, sack3):
    for char in sack1:
        if char in sack2 and char in sack3:
            return char

score = 0
for i in range(len(sacks)):
    badge = findTriple(sacks[i][0], sacks[i][1], sacks[i][2])
    score += getVal(badge)
print(score)