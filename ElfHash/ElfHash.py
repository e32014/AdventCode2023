file = open("input.txt")


def hash_alg(string):
    hash = 0
    for chr in string:
        hash += ord(chr)
        hash *= 17
        hash = hash % 256
    return hash


content = []
for line in file:
    content = line.strip().split(",")

total = 0
hashmap = dict()
for step in content:
    if '=' in step:
        key, lens = step.split("=")[:2]
        hashed = hash_alg(key)
        if hashed in hashmap:
            hashmap[hashed] = [i if i[0] != key else (key, lens) for i in hashmap[hashed]]
            if (key, lens) not in hashmap[hashed]:
                hashmap[hashed].append((key, lens))
        else:
            hashmap[hashed] = [(key, lens)]
    if '-' in step:
        key = step[:-1]
        hashed = hash_alg(key)
        if hashed in hashmap:
            hashmap[hashed] = [i for i in hashmap[hashed] if i[0] != key]

total = 0
for box, val in hashmap.items():
    for pos, (key, lens) in enumerate(val):
        total += (box + 1) * (pos + 1) * int(lens)
print(total)