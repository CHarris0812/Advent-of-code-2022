data = ""

f = open("Day 6 input.txt", "r")
data = f.read()

pastFour = [*data[:14]]

def moveBack(l):
    temp = []
    for i in range(1, len(l)):
        temp.append(l[i])
    temp.append("")
    return temp

def allDifferent(l):
    return len(set(l)) == len(l)

for i in range(14, len(data)):
    print(i)
    pastFour = moveBack(pastFour)
    pastFour[-1] = data[i]
    if allDifferent(pastFour):
        print(i + 1)
        break
