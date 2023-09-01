assignments = []

f = open("Day 4 input.txt", "r")
for line in f:
    line = line.replace("\n", "")
    temp = line.split(",")
    temp = [temp[0].split("-"), temp[1].split("-")]
    temp = [[int(j) for j in i] for i in temp]
    assignments.append(temp)


def fullyInside(pair1, pair2):
    if (pair1[1] >= pair2[1] and pair1[0] <= pair2[0]) or (pair2[1] >= pair1[1] and pair2[0] <= pair1[0]):
        return True
    return False

count = 0
for i in assignments:
    if fullyInside(i[0], i[1]):
        count += 1
print(count)

def overlap(pair1, pair2):
    if (pair1[0] <= pair2[0] and pair1[1] >= pair2[0]) or (pair1[0] <= pair2[1] and pair1[1] >= pair2[1]) or (pair2[0] <= pair1[0] and pair2[1] >= pair1[0]) or (pair2[0] <= pair1[1] and pair2[1] >= pair1[1]):
        return True
    return False

count = 0
for i in assignments:
    if overlap(i[0], i[1]):
        count += 1
print(count)