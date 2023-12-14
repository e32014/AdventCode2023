import copy

file = open("input.txt")


def hash(graph):
    return "".join(["".join(line) for line in graph])


def dropThem(graph):
    lowest_pos = [0 for _ in range(len(graph[0]))]
    for y, line in enumerate(graph):
        for x, char in enumerate(line):
            if char == '#':
                lowest_pos[x] = y + 1
            if char == 'O':
                graph[y][x] = '.'
                graph[lowest_pos[x]][x] = 'O'
                lowest_pos[x] += 1


def rotate(graph):
    new_graph = copy.deepcopy(graph)
    for y, line in enumerate(graph):
        for x, char in enumerate(line):
            new_graph[x][len(graph) - y - 1] = char
    return new_graph


graph = []
for line in file:
    graph.append(list(line.strip()))

seen = dict()
moved = []
cycle = 1_000_000_000
rest = 0
for cycle_i in range(cycle):
    hashed = hash(graph)
    if hashed in seen:
        start = seen[hashed]
        length = cycle_i - start
        rest = cycle - ((cycle - start) // length) * length - start
        break

    seen[hashed] = cycle_i
    for _ in range(4):
        dropThem(graph)
        graph = rotate(graph)

for _ in range(rest):
    for _ in range(4):
        dropThem(graph)
        graph = rotate(graph)

for line in graph:
    print(line)
total = 0
for y, line in enumerate(graph):
    for char in line:
        if char == 'O':
            total += len(graph) - y
print(total)