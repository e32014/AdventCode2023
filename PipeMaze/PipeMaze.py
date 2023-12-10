file = open("input.txt")

grid = []
sPos = (0, 0)
for line in file:
    grid.append(line.strip())
    if 'S' in grid[-1]:
        sPos = (grid[-1].index('S'), len(grid) - 1)

for i in range(len(grid)):
    print(i, grid[i])
print(sPos)

queue = [sPos]
visited = {sPos: 0}
currMax = 0
startUp = False
while len(queue) > 0:
    currPosX, currPosY = queue.pop(0)
    if grid[currPosY][currPosX] == 'S':
        if currPosY - 1 >= 0 and grid[currPosY - 1][currPosX] in ("|", "7", "F") and (currPosX, currPosY - 1) not in visited:
            queue.append((currPosX, currPosY - 1))
            visited[(currPosX, currPosY - 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY - 1)])
            startUp = True
        if currPosY + 1 < len(grid) and grid[currPosY + 1][currPosX] in ("|", "J", "L") and (currPosX, currPosY + 1) not in visited:
            queue.append((currPosX, currPosY + 1))
            visited[(currPosX, currPosY + 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY + 1)])
        if currPosX - 1 >= 0 and grid[currPosY][currPosX - 1] in ("-", "L", "F") and (currPosX - 1, currPosY) not in visited:
            queue.append((currPosX - 1, currPosY))
            visited[(currPosX - 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX - 1, currPosY)])
        if currPosX + 1 < len(grid[currPosY]) and grid[currPosY][currPosX + 1] in ("-", "J", "7") and (currPosX + 1, currPosY) not in visited:
            queue.append((currPosX + 1, currPosY))
            visited[(currPosX + 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX + 1, currPosY)])
    elif grid[currPosY][currPosX] == '|':
        if currPosY - 1 >= 0 and (currPosX, currPosY - 1) not in visited:
            queue.append((currPosX, currPosY - 1))
            visited[(currPosX, currPosY - 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY - 1)])
        if currPosY + 1 < len(grid) and (currPosX, currPosY + 1) not in visited:
            queue.append((currPosX, currPosY + 1))
            visited[(currPosX, currPosY + 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY + 1)])
    elif grid[currPosY][currPosX] == '-':
        if currPosX - 1 >= 0 and (currPosX - 1, currPosY) not in visited:
            queue.append((currPosX - 1, currPosY))
            visited[(currPosX - 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX - 1, currPosY)])
        if currPosX + 1 < len(grid[currPosY]) and (currPosX + 1, currPosY) not in visited:
            queue.append((currPosX + 1, currPosY))
            visited[(currPosX + 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX + 1, currPosY)])
    elif grid[currPosY][currPosX] == 'L':
        if currPosY - 1 >= 0 and (currPosX, currPosY - 1) not in visited:
            queue.append((currPosX, currPosY - 1))
            visited[(currPosX, currPosY - 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY - 1)])
        if currPosX + 1 < len(grid[currPosY]) and (currPosX + 1, currPosY) not in visited:
            queue.append((currPosX + 1, currPosY))
            visited[(currPosX + 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX + 1, currPosY)])
    elif grid[currPosY][currPosX] == 'J':
        if currPosY - 1 >= 0 and (currPosX, currPosY - 1) not in visited:
            queue.append((currPosX, currPosY - 1))
            visited[(currPosX, currPosY - 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY - 1)])
        if currPosX - 1 >= 0 and (currPosX - 1, currPosY) not in visited:
            queue.append((currPosX - 1, currPosY))
            visited[(currPosX - 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX - 1, currPosY)])
    elif grid[currPosY][currPosX] == '7':
        if currPosY + 1 < len(grid) and (currPosX, currPosY + 1) not in visited:
            queue.append((currPosX, currPosY + 1))
            visited[(currPosX, currPosY + 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY + 1)])
        if currPosX - 1 >= 0 and (currPosX - 1, currPosY) not in visited:
            queue.append((currPosX - 1, currPosY))
            visited[(currPosX - 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX - 1, currPosY)])
    elif grid[currPosY][currPosX] == 'F':
        if currPosY + 1 < len(grid) and (currPosX, currPosY + 1) not in visited:
            queue.append((currPosX, currPosY + 1))
            visited[(currPosX, currPosY + 1)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX, currPosY + 1)])
        if currPosX + 1 < len(grid[currPosY]) and (currPosX + 1, currPosY) not in visited:
            queue.append((currPosX + 1, currPosY))
            visited[(currPosX + 1, currPosY)] = visited[(currPosX, currPosY)] + 1
            currMax = max(currMax, visited[(currPosX + 1, currPosY)])

print(currMax)

total = 0
for y in range(len(grid)):
    crossed = 0
    for x in range(len(grid[y])):
        if (x, y) in visited:
            if grid[y][x] in ['J', 'L', '|'] or (grid[y][x] == 'S' and startUp):
                crossed += 1
        elif crossed % 2 == 1:
            total += 1
print(total)