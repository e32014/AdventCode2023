import math
import re

file = open('input.txt')

path = file.readline().strip()

file.readline()
nodes = dict()
entry = file.readline()
currs = []
while entry != "":
    node, left, right = re.match("([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)", entry.strip()).groups()
    nodes[node] = (left, right)
    if node[-1] == 'A':
        currs.append(node)
    elif node[-1] == 'Z':
        print((left, right))
    entry = file.readline()

allSteps = []
for curr in currs:
    steps = 0
    while curr[-1] != 'Z':
        if path[steps % len(path)] == 'R':
            curr = nodes[curr][1]
        else:
            curr = nodes[curr][0]
        steps += 1
    allSteps.append(steps)
print(math.lcm(*allSteps))
print(allSteps)