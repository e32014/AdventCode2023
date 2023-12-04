file = open("input.txt")

content = []
scoreCards = dict()
counts = dict()
total = 0
for line in file:
    wins = []
    card, nums = line.strip().split(":")
    got, winners = nums.split("|")
    got = [int(i) for i in got.split()]
    winners = set(int(i) for i in winners.split())
    for val in got:
        if val in winners:
            wins.append(got)
    scoreCards[int(card.split()[1])] = len(wins)
    counts[int(card.split()[1])] = 1

pos = 1
while pos in scoreCards:
    for i in range(1, scoreCards[pos] + 1):
        counts[pos + i] += 1 * counts[pos]
    pos += 1
print(counts)
print(sum(counts.values()))