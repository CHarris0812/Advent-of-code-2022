f = open("Day 13 input.txt", "r")

data = []
temp = ""
for line in f:
    line = line.replace("\n", "")
    if line == "":
        temp = ""
    elif temp == "":
        temp = line
    else:
        data.append([eval(temp), eval(line)])


def inOrder(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return True
        if second < first:
            return False
        return None
    
    if type(first) == int:
        first = [first]
    if type(second) == int:
        second = [second]

    for i in range(len(first)):
        if len(second) < i + 1:
            return False
        if inOrder(first[i], second[i]) != None:
            return inOrder(first[i], second[i])

    if len(second) > len(first):
        return True
    return None



sum = 0
for i in range(len(data)):
    arr1 = data[i][0]
    arr2 = data[i][1]
    
    correct = inOrder(arr1, arr2)
    if correct == None:
        print("shit")

    if correct:
        sum += i + 1

print(sum)


f = open("Day 13 input.txt", "r")
data = []
for line in f:
    line = line.replace("\n", "")
    if line != "":
        data.append(eval(line))

sorted = [[[2]], [[6]]]
for i in data:
    s = False
    for j in range(len(sorted)):
        if not s:
            if inOrder(i, sorted[j]):
                sorted = sorted[:j] + [i] + sorted[j:]
                s = True


first = 0
second = 0
for i in range(len(sorted)):
    if sorted[i] == [[2]]:
        first = i + 1
    if sorted[i] == [[6]]:
        second = i + 1
print(first * second)
#print(sorted)