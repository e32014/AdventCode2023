import copy
import heapq

file = open("input.txt")

graph = []
start = (1, 0)
for line in file:
    graph.append(line.strip())
end = (len(graph[0]) - 2, len(graph) - 1)

print(start, end)
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
permissible = ['>', 'v', '<', '^', '.']
node_graph = dict()
for y, row in enumerate(graph):
    for x, val in enumerate(row):
        if graph[y][x] not in permissible:
            continue
        routes = 0
        for i, dir in enumerate(dirs):
            delta_x = x + dir[0]
            delta_y = y + dir[1]
            if delta_x < 0 or delta_x >= len(graph[0]) or delta_y < 0 or delta_y >= len(graph):
                continue
            if graph[delta_y][delta_x] in permissible:
                routes += 1
        if routes > 2:
            node_graph[(x, y)] = []

print(node_graph)
node_graph[start] = []
node_graph[end] = []
queue = [(0, start)]
for node in node_graph.keys():
    queue = [(0, node)]
    visited = set()
    while queue:
        curr, pos = queue.pop(0)
        visited.add(pos)
        if pos != node and pos in node_graph:
            node_graph[pos].append((curr, node))
            continue
        for i, dir in enumerate(dirs):
            delta_x = dir[0] + pos[0]
            delta_y = dir[1] + pos[1]
            if delta_x < 0 or delta_x >= len(graph[0]) or delta_y < 0 or delta_y >= len(graph):
                continue
            if (graph[delta_y][delta_x] == '.' or graph[delta_y][delta_x] in permissible) and (delta_x, delta_y) not in visited:
                queue.append((curr + 1, (delta_x, delta_y)))

stack = [(0, start, set())]
max = 0
while stack:
    score, pos, visited = stack.pop()
    visited.add(pos)
    if pos == end and score > max:
        max = score
    for cost, node in node_graph[pos]:
        if node not in visited:
            stack.append((score + cost, node, copy.copy(visited)))
print(max)