from math import floor, sqrt, ceil

file = open('input.txt')

content = []
times = []
dists = []
for line in file:
    content.append(line.strip())

times = [int("".join(content[0].split(":")[1].strip().split()))]
dists = [int("".join(content[1].split(":")[1].strip().split()))]
#times = [int(i) for i in content[0].split(":")[1].split()]
#dists = [int(i) for i in content[1].split(":")[1].split()]
pairs = list(zip(times, dists))

product = 1
for time, record in pairs:
    low = ceil((-1 * time + sqrt(time ** 2 - 4 * record))/-2)
    high = ceil((-1 * time - sqrt(time ** 2 - 4 * record))/-2)
    print(low, high)
    count = high - low
    if -1 * high ** 2 + time * high - record == 0:
        count -= 1
    product *= count

print(product)