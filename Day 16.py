import time

def part1():
    valveToFlow = {}
    valveToNeighbors = {}
    possibleValvesToOpen = []
    valveToValves = {}

    f = open("Day 16 input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        temp = line.split(";")

        valve = temp[0][6:8]
        flow = int(temp[0][23:])

        temp[1] = temp[1].replace(" tunnels lead to valves ", "")
        temp[1] = temp[1].replace(" tunnel leads to valve ", "")
        neighbors = temp[1].split(", ")

        if flow != 0:
            possibleValvesToOpen.append(valve)

        valveToFlow[valve] = flow
        valveToNeighbors[valve] = neighbors


    importantValves = ["AA"] + possibleValvesToOpen

    for valve in importantValves:
        temp = [(0, valve)]
        visited = []

        while(len(temp) > 0):
            temp.sort()
            cur = temp.pop(0)

            time = cur[0]
            v = cur[1]

            if v not in visited:
                visited.append(v)
                if v in importantValves:
                    valveToValves[(valve, v)] = time

                for neighbor in valveToNeighbors[v]:
                    temp.append((time + 1, neighbor))


    #(minute, total, current, location, open]
    options = [(1, 0, 0, "AA", ["AA"])]
    results = []
    totalMinutes = 30
    maxSeen = 0

    while len(options) > 0:
        options.sort()
        temp = options.pop(0)
        minute = temp[0]
        totalFlow = temp[1]
        curFlow = temp[2]
        location = temp[3]
        openValves = temp[4]
        if minute > maxSeen:
            maxSeen = minute
            print(minute)

        if minute <= totalMinutes:
            if len(openValves) == len(importantValves):
                results.append(totalFlow + curFlow * (totalMinutes - minute + 1))
            else:
                if location not in openValves:
                    options.append((minute + 1, totalFlow + curFlow, curFlow + valveToFlow[location], location, openValves + [location]))
                else:
                    for valve in importantValves:
                        if valve not in openValves:
                            timeToVisit = valveToValves[(location, valve)]
                            options.append((minute + timeToVisit, totalFlow + curFlow * timeToVisit, curFlow, valve, openValves))
                    results.append(totalFlow + curFlow * (totalMinutes - minute + 1))

    print(max(results))

def readData():
    flows = {}
    neighbors = {}
    importantValves = []
    f = open("Day 16 input.txt", "r")
    for line in f:
        line = line.replace("\n", "")
        temp = line.split(";")

        valve = temp[0][6:8]
        flow = int(temp[0][23:])

        temp[1] = temp[1].replace(" tunnels lead to valves ", "")
        temp[1] = temp[1].replace(" tunnel leads to valve ", "")
        nbors = temp[1].split(", ")

        flows[valve] = flow
        neighbors[valve] = nbors
        if flow != 0:
            importantValves.append(valve)
    return flows, neighbors, importantValves

def shortestPath(loc, goal, neighbors, visited):
    if loc == goal:
        return [goal]
    
    minPathLength = 1000
    minPath = ["" for i in range(100)]
    for valve in neighbors[loc]:
        if valve not in visited:
            temp = shortestPath(valve, goal, neighbors, visited + [loc])
            if len(temp) < minPathLength:
                minPathLength = len(temp)
                minPath = temp
    return [loc] + minPath

def findPaths(flow, neighbors):
    paths = {valve:{v:[] for v in flow} for valve in flow}
    
    for valve in flow:
        for goalValve in flow:
            if valve in importantValves and goalValve in importantValves:
                paths[valve][goalValve] = shortestPath(valve, goalValve, neighbors, [])
    return paths

'''
def run(minute, hLoc, eLoc, openValves, pressureReleased, currentRate, hDissalowed, eDissalowed):
    global maxReleased

    if minute == maxMinutes:
        if pressureReleased > maxReleased:
            maxReleased = pressureReleased
            print(pressureReleased)
        return pressureReleased

    maxVal = 0
    pressureReleased += currentRate
    if pressureReleased + theoreticalReleaseRate * (maxMinutes - minute) < maxReleased:
        return pressureReleased


    if flow[hLoc] != 0 and hLoc not in openValves:
        if flow[eLoc] != 0 and eLoc not in openValves and eLoc != hLoc:
            maxVal = max(maxVal, run(minute + 1, hLoc, eLoc, openValves + [hLoc, eLoc], pressureReleased, 
                                 currentRate + flow[hLoc] + flow[eLoc], [], []))


        for nextMoveE in neighbors[eLoc]:
            maxVal = max(maxVal, run(minute + 1, hLoc, nextMoveE, openValves + [hLoc], pressureReleased, 
                                 currentRate + flow[hLoc], [], eDissalowed + [eLoc]))

    if flow[eLoc] != 0 and eLoc not in openValves:
        for nextMoveH in neighbors[hLoc]:
            maxVal = max(maxVal, run(minute + 1, nextMoveH, eLoc, openValves + [eLoc], pressureReleased, 
                                 currentRate + flow[eLoc], [hDissalowed] + [hLoc], []))

    for nextMoveH in neighbors[hLoc]:
        for nextMoveE in neighbors[eLoc]:
            if nextMoveH not in hDissalowed and nextMoveE not in eDissalowed:
                maxVal = max(maxVal, run(minute + 1, nextMoveH, nextMoveE, openValves, pressureReleased, currentRate, 
                                         hDissalowed + [hLoc], eDissalowed + [eLoc]))

    if maxVal == 0:
        return pressureReleased + currentRate * (maxMinutes - minute - 1)
    return maxVal
'''

def firstRun():
    for valve in range(len(importantValves)):
        for v in range(valve):
            t = time.time()
            ePath = paths["AA"][importantValves[valve]]
            hPath = paths["AA"][importantValves[v]]
            minLength = min(len(ePath), len(hPath)) - 1
            run(minLength, ePath[minLength:], hPath[minLength:], 0, [importantValves[valve], importantValves[v]])
            print(time.time() - t)
            

def run(minute, ePath, hPath, flowReleased, openValves):
    global maxReleased

    if flowReleased > maxReleased:
        maxReleased = flowReleased
        print(maxReleased)

    if minute >= 26:
        pass
            
        
    #If at end for both
    elif len(ePath) == 1 and len(hPath) == 1:


        #Open both valves
        flowReleased += flow[ePath[0]] * (25 - minute)
        flowReleased += flow[hPath[0]] * (25 - minute)        

        if len(openValves) == len(importantValves):
            run(100, [], [], flowReleased, [])
        else:
            for valve in importantValves:
                for v in importantValves:
                    if valve != v and valve not in openValves and v not in openValves:
                        ePath = paths[ePath[0]][valve]
                        hPath = paths[hPath[0]][v]
                        minLength = min(len(ePath), len(hPath)) - 1
                        run(minute + minLength + 1, ePath[minLength:], hPath[minLength:], flowReleased, openValves + [valve, v])
                    
    elif len(ePath) == 1:
        flowReleased += flow[ePath[0]] * (25 - minute)
        
        if len(openValves) == len(importantValves):
            tempFlow = flow[hPath[-1]] * (26 - minute - len(hPath))
            run(100, [], [], flowReleased + tempFlow, [])
        else:
            for valve in importantValves:
                if valve not in openValves:
                    ePath = [ePath[0]] + paths[ePath[0]][valve]
                    minLength = min(len(ePath), len(hPath)) - 1
                    run(minute + minLength, ePath[minLength:], hPath[minLength:], flowReleased, openValves + [valve])


    elif len(hPath) == 1:
        flowReleased += flow[hPath[0]] * (25 - minute)

        if len(openValves) == len(importantValves):
            tempFlow = flow[ePath[-1]] * (26 - minute - len(ePath))
            run(100, [], [], flowReleased + tempFlow, [])
        else:
            for valve in importantValves:
                if valve not in openValves:
                    hPath = [hPath[0]] + paths[hPath[0]][valve]
                    minLength = min(len(ePath), len(hPath)) - 1
                    run(minute + minLength, ePath[minLength:], hPath[minLength:], flowReleased, openValves + [valve])

    else:
        print("shit")



flow, neighbors, importantValves = readData()
importantValves = ["AA"] + importantValves
paths = findPaths(flow, neighbors)
importantValves = importantValves[1:]

maxReleased = 0
theoreticalReleaseRate = sum([flow[i] for i in flow])
maxMinutes = 26
firstRun()

'''
Valve AA has flow rate=0; tunnel leads to valve BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA, DD
Valve CC has flow rate=2; tunnel leads to valve BB, DD
Valve DD has flow rate=100; tunnels lead to valves CC, BB
'''