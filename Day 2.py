oppMoves = []
playerMoves = []
xyzToabc = {"X":"A", "Y":"B", "Z":"C"}
scores = {"X":1, "Y":2, "Z":3}

f = open("Day 2 input.txt", "r")
for line in f:
    oppMoves.append(line[0])
    playerMoves.append(line[2])

def didPlayerWin(oppMove, pMove):
    playerMove = xyzToabc[pMove]
    if playerMove == oppMove:
        return 3
    if (playerMove == "A" and oppMove == "C") or (playerMove == "B" and oppMove == "A") or (playerMove == "C" and oppMove == "B"):
        return 6
    return 0

totalScore = 0
for i in range(2500):
    totalScore += scores[playerMoves[i]]
    totalScore += didPlayerWin(oppMoves[i], playerMoves[i])

print(totalScore)

#Part 2
goals = playerMoves
scores = {"A":1, "B":2, "C":3}
whatLoses = {"A":"C", "B":"A", "C":"B"}
whatWins = {"A":"B", "B":"C", "C":"A"}
scoreFromResult = {"X":0, "Y":3, "Z":6}

def getMove(oppMove, goal):
    if goal == "Y":
        return oppMove
    if goal == "X":#Lose
        return whatLoses[oppMove]
    return whatWins[oppMove]

totalScore = 0
for i in range(2500):
    playerMove = getMove(oppMoves[i], goals[i])
    totalScore += scores[playerMove]
    totalScore += scoreFromResult[goals[i]]

print(totalScore)