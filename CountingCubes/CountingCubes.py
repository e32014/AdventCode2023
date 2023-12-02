import re

file = open("input.txt")

total = 0
for line in file:
    maxes = {"red": 0, "green": 0, "blue": 0}
    id, games = line.strip().split(":")
    id = int(re.match("Game ([0-9]+)", id).group(1))
    valid = True
    for game in games.split(";"):
        for rev in game.split(","):
            amount, color = re.match("([0-9]+) ([a-zA-Z]+)", rev.strip()).groups()
            if maxes[color] < int(amount):
                maxes[color] = int(amount)
    mult = 1
    for val in maxes.values():
        mult *= val
    total += mult

print(total)