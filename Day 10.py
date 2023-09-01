action = []

f = open("Day 10 input.txt", "r")
for line in f:
    line = line.replace("\n", "")
    if "noop" in line:
        action.append(["noop", 0])
    else:
        temp = line.split(" ")
        if temp[1][0] == "-":
            action.append([temp[0], -1 * int(temp[1][1:])])
        else:
            action.append([temp[0], int(temp[1])])


cycle = 0
counter = 1
storedVals = []
for i in action:
    if i[0] == "noop":
        cycle += 1
        if cycle % 40 == 20:
            storedVals.append(counter * cycle)
    else:
        cycle += 1
        if cycle % 40 == 20:
            storedVals.append(counter * cycle)
        cycle += 1
        if cycle % 40 == 20:
            storedVals.append(counter * cycle)
        counter += i[1]
print(storedVals)
print(sum(storedVals))


def addPixel(display, cycle, location):
    if abs(cycle % 40 - location) <= 1:
        display += "#"
    else:
        display += "."
    return display

display = ""
cycle = 0
counter = 1
for i in action:
    if i[0] == "noop":
        display = addPixel(display, cycle, counter)
        cycle += 1
        if cycle % 40 == 0:
            display += "\n"
    else:
        display = addPixel(display, cycle, counter)
        cycle += 1
        if cycle % 40 == 0:
            display += "\n"
        display = addPixel(display, cycle, counter)
        cycle += 1
        if cycle % 40 == 0:
            display += "\n"
        counter += i[1]

print(display)
