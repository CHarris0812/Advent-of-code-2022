import time
monkeys, tempMonkeys, f = {}, [], open("Day 21 input.txt", "r")
for line in f:
    tempMonkeys.append([line.replace("\n", "").replace(":", "="), line.replace("\n", "")[6:].split(" ")])
while "root" not in monkeys:
    for m in tempMonkeys:
        if len(m[1]) == 1: monkeys[m[0][:4]] = eval(m[0][6:])
        elif m[1][0] in monkeys and m[1][2] in monkeys: monkeys[m[0][:4]] = eval("monkeys[\"" + m[1][0] + "\"]" + m[1][1] + "monkeys[\"" + m[1][2] + "\"]")         
print(int(monkeys["root"]))


monkeys = {}
rootEquations = ["", ""]
done = False
while not done:
    for m in tempMonkeys:
        if m[0][:4] == "humn":
            monkeys["humn"] = "humn"
        elif len(m[1]) == 1:
            monkeys[m[0][:4]] = m[0][6:]
        elif m[1][0] in monkeys and m[1][2] in monkeys:
            if m[0][:4] == "root":
                rootEquations[0] = monkeys[m[1][0]]
                rootEquations[1] = monkeys[m[1][2]]
                done = True
            else:
                if "humn" not in monkeys[m[1][0]] and "humn" not in monkeys[m[1][2]]:
                    monkeys[m[0][:4]] = str(int(eval(monkeys[m[1][0]] + m[1][1] + monkeys[m[1][2]])))
                else:
                    monkeys[m[0][:4]] = "(" + monkeys[m[1][0]] + m[1][1] + monkeys[m[1][2]] + ")"


print(rootEquations[0])
print(rootEquations[1])

import re
def simplifyEquation(equation, value):
    if re.findall("^\(\d+\*", equation) != []:
        temp = re.findall("^\(\d+\*", equation)
        number = re.findall("\d+", temp[0])
        value = value // float(number[0])
        equation = equation[len(temp[0]):-1]
        return equation, value
    if re.findall("^\(\d+\+", equation) != []:
        temp = re.findall("^\(\d+\+", equation)
        number = re.findall("\d+", temp[0])
        value = value - float(number[0])
        equation = equation[len(temp[0]):-1]
        return equation, value
    if re.findall("^\(\d+\/", equation) != []:
        temp = re.findall("^\(\d+\/", equation)
        number = re.findall("\d+", temp[0])
        value = float(number[0]) / value
        equation = equation[len(temp[0]):-1]
        return equation, value
    if re.findall("^\(\d+-", equation) != []:
        temp = re.findall("^\(\d+-", equation)
        number = re.findall("\d+", temp[0])
        value = -(value - float(number[0]))
        equation = equation[len(temp[0]):-1]
        return equation, value


    if re.findall("\*\d+\)$", equation) != []:
        temp = re.findall("\*\d+\)$", equation)
        number = re.findall("\d+", temp[0])
        value = value // float(number[0])
        equation = equation[1:-len(temp[0])]
        return equation, value
    if re.findall("\+\d+\)$", equation) != []:
        temp = re.findall("\+\d+\)$", equation)
        number = re.findall("\d+", temp[0])
        value = value - float(number[0])
        equation = equation[1:-len(temp[0])]
        return equation, value
    if re.findall("\/\d+\)$", equation) != []:
        temp = re.findall("\/\d+\)$", equation)
        number = re.findall("\d+", temp[0])
        value = value * float(number[0])
        equation = equation[1:-len(temp[0])]
        return equation, value
    if re.findall("-\d+\)$", equation) != []:
        temp = re.findall("-\d+\)$", equation)
        number = re.findall("\d+", temp[0])
        value = value + float(number[0])
        equation = equation[1:-len(temp[0])]
        return equation, value
    return equation, value

rootEquations[1] = int(float(rootEquations[1]))

while(rootEquations[0] != "humn"):
    rootEquations[0], rootEquations[1] = simplifyEquation(rootEquations[0], rootEquations[1])
print(rootEquations[1])