file = open("input.txt")


def checker(springs, groups, groupi, i, counter, memo):
    key = (groupi, i, counter)
    if key in memo:
        return memo[key]
    if i == len(springs):
        if groupi == len(groups) and counter == 0:
            return 1
        elif groupi == len(groups) - 1 and groups[groupi] == counter:
            return 1
        else:
            return 0

    ans = 0
    if springs[i] == '.':
        if counter > 0 and groupi < len(groups) and groups[groupi] == counter:
            ans += checker(springs, groups, groupi + 1, i + 1, 0, memo)
        elif counter == 0:
            ans += checker(springs, groups, groupi, i + 1, counter, memo)
    elif springs[i] == '#':
        ans += checker(springs, groups, groupi, i + 1, counter + 1, memo)
    elif springs[i] == "?":
        hash_count = checker(springs, groups, groupi, i + 1, counter + 1, memo)
        dot_count = 0
        if counter > 0 and groupi < len(groups) and groups[groupi] == counter:
            dot_count += checker(springs, groups, groupi + 1, i + 1, 0, memo)
        elif counter == 0:
            dot_count += checker(springs, groups, groupi, i + 1, counter, memo)
        ans += hash_count + dot_count
    memo[key] = ans
    return ans

rows = []
for line in file:
    springs, groups = line.strip().split()[0:2]
    springs = "?".join([springs] * 5)
    rows.append((springs, [int(x) for x in groups.split(",")] * 5))

count = 0
for row in rows:
    count += checker(row[0], row[1], 0, 0, 0, dict())
print(count)