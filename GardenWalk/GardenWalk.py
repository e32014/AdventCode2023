file = open("input.txt")

rocks = set()
start = None
max_y = 0
max_x = 0
for line in file:
    max_x = len(line.strip())
    for x in range(max_x):
        if line[x] == '#':
            rocks.add((x, max_y))
        elif line[x] == 'S':
            start = (x, max_y)
    max_y += 1

visited = set()
stepped = set()
found_pos = set()
queue = {start}
target = 26501365
comps = []
last_len = 0
for i in range(1, max_x * 3 + target % max_x):
    next_queue = set()
    for pos in queue:
        x, y = pos
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if ((x + dx) % max_x, (y + dy) % max_y) not in rocks:
                next_queue.add((x + dx, y + dy))
    queue = next_queue
    if i % max_y == target % max_y:
        print(i, len(queue), len(queue) - last_len, i // max_y)
        comps.append(len(queue))
        if len(comps) == 3:
            break
        last_len = len(queue)

a1 = comps[0]
a2 = comps[1]
a3 = comps[2]
b0 = a1
b1 = a2 - a1
b2 = a3 - a2
n = target // max_x
print(b0 + b1 * n + ((n * (n - 1)) // 2) * (b2 - b1))
print(len(queue))