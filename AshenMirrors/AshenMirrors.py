file = open("input.txt")


def find_mirror(currMap):
    for i in range(len(currMap) - 1):
        mistakes = 0
        mirror = True
        for j in range(min(i, len(currMap) - 2 - i) + 1):
            for k in range(len(currMap[i])):
                if currMap[i - j][k] != currMap[i + j + 1][k] and mistakes == 1:
                    mirror = False
                    break
                elif currMap[i -j][k] != currMap[i + j + 1][k] and mistakes == 0:
                    mistakes += 1
            if not mirror:
                break
        if mirror and mistakes > 0:
            return i + 1
    return -1


maps = []
currMap = []
for line in file:
    if line.strip() != '':
        currMap.append(line.strip())
    else:
        maps.append(currMap)
        currMap = []
maps.append(currMap)

total = 0
for currMap in maps:
   rotMap = list(map(''.join, zip(*reversed(currMap))))
   vert = find_mirror(rotMap)
   hori = find_mirror(currMap)
   if vert > 0:
       total += vert
   if hori > 0:
       total += hori * 100
print(total)