file = open("input.txt")

content = []
for line in file:
    content.append([int(i) for i in line.strip().split()])

total = 0
for seq in content:
    deltas = [seq]
    while any(v != 0 for v in deltas[-1]):
        newDelta = []
        for i in range(len(deltas[-1]) - 1):
            newDelta.append(deltas[-1][i+1] - deltas[-1][i])
        deltas.append(newDelta)
    print(deltas)
    for i in range(len(deltas) - 1, -1, -1):
        if i == len(deltas) - 1:
            deltas[i].insert(0, 0)
        else:
            deltas[i].insert(0, deltas[i][0] - deltas[i + 1][0])
    print(deltas)
    total += deltas[0][0]
print(total)