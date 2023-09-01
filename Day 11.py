import math
monkeys = []

f = open("Day 11 input.txt", "r")
temp = []
for line in f:
    if "Monkey" in line:
        temp.append(0)
        monkeys.append([i for i in temp])
        temp = []
    else:
        line = line.replace("\n", "")
        if "Starting items:" in line:
            line = line.replace("  Starting items: ", "")
            line = line.split(", ")
            line = [int(i) for i in line]
            temp.append([i for i in line])
        if "Operation:" in line:
            line = line.replace("  Operation: ", "")
            line = line.replace("new = ", "")
            line = line.replace("old", "obj")
            temp.append(line)
        if "Test: " in line:
            line = line.replace("  Test: divisible by ", "")
            temp.append(int(line))
        if "true:" in line:
            line = line.replace("    If true: throw to monkey ", "")
            temp.append(int(line))
        if "false:" in line:
            line = line.replace("    If false: throw to monkey ", "")
            temp.append(int(line))


temp.append(0)
monkeys.append([i for i in temp])
monkeys = monkeys[1:]

lcm = 1
for i in monkeys:
    lcm = lcm*i[2]//math.gcd(lcm, i[2])
print(lcm)
cycles = 10000

for i in range(cycles):
    if (i % 100 == 0):
        print(i)
    for m in range(len(monkeys)):
        for obj in monkeys[m][0]:
            monkeys[m][-1] += 1
            worry = eval(monkeys[m][1])
            worry = worry % lcm
            #worry = worry // 3
            if worry % monkeys[m][2] == 0:
                monkeys[monkeys[m][3]][0].append(worry)
            else:
                monkeys[monkeys[m][4]][0].append(worry)
        monkeys[m][0] = []

monkeyCounts = [m[-1] for m in monkeys]

maxVal = max(monkeyCounts)
monkeyCounts.remove(maxVal)
secondHighest = max(monkeyCounts)

print(maxVal * secondHighest)
