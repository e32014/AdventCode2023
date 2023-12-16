file = open("input.txt")


def hunt(graph, start):
    energized = dict()
    visited = set()
    queue = [start]
    while len(queue) > 0:
        pos = queue.pop()
        if pos in visited:
            continue

        visited.add(pos)
        energized[pos[:2]] = energized.get(pos[:2], 0) + 1
        charAt = graph[pos[1]][pos[0]]
        if charAt == '.':
            if pos[2] == 0 and pos[0] + 1 < len(graph[0]):
                queue.append((pos[0] + 1, pos[1], pos[2]))
            elif pos[2] == 1 and pos[1] + 1 < len(graph):
                queue.append((pos[0], pos[1] + 1, pos[2]))
            elif pos[2] == 2 and pos[0] - 1 >= 0:
                queue.append((pos[0] - 1, pos[1], pos[2]))
            elif pos[2] == 3 and pos[1] - 1 >= 0:
                queue.append((pos[0], pos[1] - 1, pos[2]))
        elif charAt == '\\':
            if pos[2] == 0 and pos[1] + 1 < len(graph):
                queue.append((pos[0], pos[1] + 1, 1))
            elif pos[2] == 1 and pos[0] + 1 < len(graph[0]):
                queue.append((pos[0] + 1, pos[1], 0))
            elif pos[2] == 2 and pos[1] - 1 >= 0:
                queue.append((pos[0], pos[1] - 1, 3))
            elif pos[2] == 3 and pos[0] - 1 >= 0:
                queue.append((pos[0] - 1, pos[1], 2))
        elif charAt == '/':
            if pos[2] == 0 and pos[1] - 1 >= 0:
                queue.append((pos[0], pos[1] - 1, 3))
            elif pos[2] == 1 and pos[0] - 1 >= 0:
                queue.append((pos[0] - 1, pos[1], 2))
            elif pos[2] == 2 and pos[1] + 1 < len(graph):
                queue.append((pos[0], pos[1] + 1, 1))
            elif pos[2] == 3 and pos[0] + 1 < len(graph[0]):
                queue.append((pos[0] + 1, pos[1], 0))
        elif charAt == '|':
            if pos[2] == 0 or pos[2] == 2:
                if pos[1] - 1 >= 0:
                    queue.append((pos[0], pos[1] - 1, 3))
                if pos[1] + 1 < len(graph):
                    queue.append((pos[0], pos[1] + 1, 1))
            elif pos[2] == 3 and pos[1] - 1 >= 0:
                queue.append((pos[0], pos[1] - 1, 3))
            elif pos[2] == 1 and pos[1] + 1 < len(graph):
                queue.append((pos[0], pos[1] + 1, 1))
        elif charAt == '-':
            if pos[2] == 1 or pos[2] == 3:
                if pos[0] - 1 >= 0:
                    queue.append((pos[0] - 1, pos[1], 2))
                if pos[0] + 1 < len(graph[0]):
                    queue.append((pos[0] + 1, pos[1], 0))
            elif pos[2] == 2 and pos[0] - 1 >= 0:
                queue.append((pos[0] - 1, pos[1], pos[2]))
            elif pos[2] == 0 and pos[0] + 1 < len(graph[0]):
                queue.append((pos[0] + 1, pos[1], pos[2]))
    return(len(energized))


graph = []
for line in file:
    graph.append(line.strip())

# E = 0
# S = 1
# W = 2
# N = 3
pos = (0,0, 0)
max = 0
for i in range(len(graph[0])):
    val = hunt(graph, (i, 0, 1))
    if val > max:
        max = val
    val = hunt(graph, (i, len(graph) - 1, 3))
    if val > max:
        max = val

for i in range(len(graph)):
    val = hunt(graph, (0, i, 0))
    if val > max:
        max = val
    val = hunt(graph, (len(graph[0]) - 1, i, 2))
    if val > max:
        max = val
print(max)