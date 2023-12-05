import math

file = open('input.txt')

content = []

seeds = [int(i) for i in file.readline().split(":")[1].strip().split()]
print(seeds)
file.readline()
ranges = []
for pos in range(0, len(seeds), 2):
    ranges.append((seeds[pos], seeds[pos] + seeds[pos+1]))
line = file.readline()
while line != "":
    print(ranges)
    line = file.readline()
    newRanges = []
    while line != "" and line != "\n":
        remainder = []
        dest, source, size = [int(i) for i in line.strip().split()]
        limit = source + size
        for range in ranges:
            start = range[0]
            end = range[1]
            nStart = 0
            nEnd = 0
            impact = False
            if source > start and source <= end:
                remainder.append((start, source))
                nStart = dest
                impact = True
            elif start >= source and start < limit:
                nStart = start - source + dest
                impact = True
            if limit <= end and limit > start:
                remainder.append((limit, end))
                nEnd = limit - source + dest
                impact = True
            elif end < limit and end >= source:
                nEnd = end - source + dest
                impact = True
            if impact:
                newRanges.append((nStart, nEnd))
            else:
                remainder.append(range)
        print((source, limit, dest), remainder, newRanges)
        ranges = remainder
        line = file.readline()
    if line == "\n":
        file.readline()
    ranges = newRanges + remainder

print(ranges)
smallest = math.inf
for low, _ in ranges:
    if low < smallest:
        smallest = low
print(smallest)