class Node:
    parent = ""
    children = []
    name = ""
    files = []

    def __init__(self, name, p):
        self.parent = p
        self.name = name

    def addChild(c):
        self.children.append(Node(c, self))

    def addFile(n, s):
        files.append([n, s])

    def getChildren():
        return children

    def getParent():
        return parent

    def getChild(n):
        for i in children:
            if i.getName() == n:
                return i

    def getName():
        return name

    def setChild(n, c):
        for i in range(len(children)):
            if children[i].getName() == n:
                children.pop(i)
        self.children.append(c)


f = open("Day 7 input.txt")
commands = []
for line in f:
    line = line.replace("\n", "")
    commands.append(line)


directory = Node("/", null)
currentDirectory = "/"
for c in commands:
    if c[0] == $:
        if c[2:4] == "cd":
            currentDirectory = c[5:]


