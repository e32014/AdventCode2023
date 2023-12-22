from collections import defaultdict

file = open('input.txt')

bricks = []
for line in file:
    start, end = line.strip().split("~")
    start = tuple([int(i) for i in start.split(",")])
    end = tuple([int(i) for i in end.split(",")])
    bricks.append((start, end))
bricks.sort(key= lambda ends: min(ends[0][2], ends[1][2]))

space = dict()
graph = dict()
for i, brick in enumerate(bricks):
    blob = set()
    bottom = set()
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            for z in range(brick[0][2], brick[1][2] + 1):
                blob.add((x, y, z))
                if z == brick[0][2]:
                    bottom.add((x, y, z))
    adjust = 0
    below = set()
    while all([val[2] > 1 for val in bottom]):
        next = set()
        for x, y, z in bottom:
            if (x, y, z - 1) in space:
                below.add(space[(x, y, z - 1)])
            else:
                next.add((x, y, z - 1))
        if len(below) > 0:
            break
        adjust += 1
        bottom = next
    for x, y, z in blob:
        space[(x, y, z - adjust)] = i
    if len(below) > 0:
        graph[i] = below
    else:
        graph[i] = {"ground"}

inverted_graph = defaultdict(list)
for key, supportedBy in graph.items():
    for val in supportedBy:
        if val != "ground":
            inverted_graph[val].append(key)

sky_holders = set()
for key in graph.keys():
    if key not in inverted_graph:
        inverted_graph[key].append("sky")
        sky_holders.add(key)
count = 0
for node in graph.keys():
    removed = {node}
    stack = []
    for val in inverted_graph[node]:
        if val != "sky":
            stack.append(val)
    while stack:
        next = stack.pop()
        if len(graph[next] - removed) == 0:
            removed.add(next)
        for val in inverted_graph[next]:
            if val != "sky":
                stack.append(val)
    count += len(removed) - 1
print(count)
print(graph)
print(inverted_graph)