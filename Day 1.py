elfIndex = 0
maxIndex = 0
max = 0
currentValue = 0

f = open("Day 1 input.txt", "r")
for line in f:
    if line == "\n":
        if currentValue > max:
            max = currentValue
            maxIndex = elfIndex
        currentValue = 0
        elfIndex += 1
    else:
        currentValue += int(line[:len(line) - 1])

print("max val", max)
print("max index", maxIndex)


#Part 2
print("Part 2")
elfCalories = []
currentValue = 0
f = open("Day 1 input.txt", "r")
for line in f:
    if line == "\n":
        elfCalories.append(currentValue)
        currentValue = 0
    else:
        currentValue += int(line[:len(line) - 1])

elfCalories.sort()
print(elfCalories)
print("Total of top 3", elfCalories[-1] + elfCalories[-2] + elfCalories[-3])