import re
blueprints = {}
maxMinutes = 32

f = open("Day 19 input.txt")
for line in f:
    line = line.replace("\n", "")
    line = line.replace("Blueprint ", "")
    line = line.replace(" Each ore robot costs", "")
    line = line.replace(" Each clay robot costs", "")
    line = line.replace(" Each obsidian robot costs", "")
    line = line.replace(" Each geode robot costs", "")
    line = line[:-1]
    
    temp = line.split(": ")
    id = temp[0]
    
    rbs = temp[1].split(". ")
    robotCosts = []
    
    for i in range(len(rbs)):
        string = rbs[i]
        
        cost = [0, 0, 0, 0]
        oreCost = re.findall("\d+ ore", string)
        if len(oreCost) != 0:
            oreCost = oreCost[0].split(" ")[0]
            oreCost = int(oreCost)
            cost[0] = oreCost
        
        clayCost = re.findall("\d+ clay", string)
        if len(clayCost) != 0:
            clayCost = clayCost[0].split(" ")[0]
            clayCost = int(clayCost)
            cost[1] = clayCost
        
        obsidianCost = re.findall("\d+ obsidian", string)
        if len(obsidianCost) != 0:
            obsidianCost = obsidianCost[0].split(" ")[0]
            obsidianCost = int(obsidianCost)
            cost[2] = obsidianCost
            
        robotCosts.append(cost)
        
    robotCosts.append([0, 0, 0, 0])
    blueprints[id] = robotCosts
    
    
def runBlueprint(minute, robotCosts, maxMinutes, maxFound, robots, ores, maxNecessary, allowed, path):
    if minute >= maxMinutes:
        return [ores[-1], path]
            
    #if maxFound[0] >= ores[-1] + robots[-1] * (maxMinutes - minute - 1) + (maxMinutes - minute) * ((maxMinutes - minute) // 2 + 1):
    #    return [0, path]
      
    minute += 1
    newOres = [ores[i] + robots[i] for i in range(4)]
    canBuyNextTurn = [a for a in allowed]
    for robotIndex in range(len(robotCosts)):
        if all([ores[i] >= robotCosts[robotIndex][i] for i in range(4)]):
            if robotIndex < 4:
                canBuyNextTurn[robotIndex] = False
                if allowed[robotIndex]:
                    if ores[robotIndex] < (maxNecessary[robotIndex] - robots[robotIndex]) * (maxMinutes - minute):
                        tempRobots = [i for i in robots]
                        tempRobots[robotIndex] += 1
                        tempOres = [newOres[i] - robotCosts[robotIndex][i] for i in range(4)]
                        tempMax = runBlueprint(minute, robotCosts, maxMinutes, maxFound, tempRobots, tempOres, maxNecessary, [True, True, True, True], path + [robotIndex])
                        if tempMax[0] > maxFound[0]:
                            maxFound = tempMax
            else:

                tempMax = runBlueprint(minute, robotCosts, maxMinutes, maxFound, [r for r in robots], [o for o in newOres], maxNecessary, canBuyNextTurn, path + [robotIndex])
                if tempMax[0] > maxFound[0]:
                    maxFound = tempMax
    return maxFound
    
    
def findMaxNecessary(bp):
    maxNecessary = [0, 0, 0, 10000]
    for i in bp:
        for j in range(4):
            maxNecessary[j] = max(maxNecessary[j], i[j])
    return maxNecessary

    
results = []
for bp in blueprints:
    maxNecessary = findMaxNecessary(blueprints[bp])
    robotCosts = blueprints[bp]
    minute = 0
    results.append(runBlueprint(minute, robotCosts, maxMinutes, [0, []], [1, 0, 0, 0], [0, 0, 0, 0], maxNecessary, [True, True, True, True], []))
    print(bp, end = " ")
    print("done")

print(results)

#vals = [(i + 1) * results[i][0] for i in range(len(results))]
#print(vals)
#print(sum(vals))
print(results[0][0] * results[1][0] * results[2][0])