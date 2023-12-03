import string
import math

file = open('input.txt')

content = []
for line in file:
    content.append([char for char in line.strip()])

digits = set(string.digits)
total = 0
covered = set()
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == '*':
            found = []
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if (di == 0 and dj == 0) or (0 > i + di >= len(content)) or (0 > j + dj >= len(content[i])):
                        continue
                    if content[i + di][j + dj] in digits and (i + di, j + dj) not in covered:
                        leftCheck = -1
                        num = content[i+di][j + dj]
                        covered.add((i + di, j + dj))
                        while j + dj + leftCheck >= 0 and content[i + di][j + dj + leftCheck] in digits:
                            num = content[i + di][j + dj + leftCheck] + num
                            covered.add((i + di, j + dj + leftCheck))
                            leftCheck -= 1
                        rightCheck = 1
                        while j + dj + rightCheck < len(content[i]) and content[i + di][j + dj + rightCheck] in digits:
                            num = num + content[i + di][j + dj + rightCheck]
                            covered.add((i + di, j + dj + rightCheck))
                            rightCheck += 1
                        found.append(int(num))
            if len(found) == 2:
                total += math.prod(found)
print(total)