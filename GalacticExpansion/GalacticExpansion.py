file = open("input.txt")

universe = set()
rows = dict()
cols = dict()
y = 0
maxX = 0
for line in file:
    if len(line.strip()) > maxX:
        maxX = len(line.strip())
    rows[y] = []
    for x in range(len(line.strip())):
        if line[x] == '#':
            universe.add((x, y))
            cols[x] = cols.get(x, []) + [(x, y)]
            rows[y].append((x, y))
    y += 1

print(universe)

emptyCols = []
for x in range(maxX):
    if x not in cols or len(cols[x]) == 0:
        emptyCols.append(x)
emptyRows = []
for j in range(y):
    if j not in rows or len(rows[j]) == 0:
        emptyRows.append(j)
print(emptyCols, emptyRows)

newUniverse = set()
for x, y in universe:
    deltaX = 0
    deltaY = 0
    for col in emptyCols:
        if x > col:
            deltaX += 999_999
    for row in emptyRows:
        if y > row:
            deltaY += 999_999
    print(x, deltaX, y, deltaY)
    newUniverse.add((x + deltaX, y + deltaY))

total = 0
visited = set()
for x1, y1 in newUniverse:
    for x2, y2 in newUniverse:
        if (x2, y2, x1, y1) in visited or (x2 == x1 and y2 == y1):
            continue
        total += abs(x2 - x1) + abs(y2 - y1)
        visited.add((x1, y1, x2, y2))
print(total)