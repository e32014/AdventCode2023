import re


def calcRange(pos, ranges, rule_dict):
    result = []
    if pos == 'R':
        return []
    if pos == 'A':
        return [ranges]
    rules = rule_dict[pos]
    for rule in rules:
        if len(rule) == 1:
            result.extend(calcRange(rule[0], ranges, rule_dict))
        else:
            (key, op, val), goto = rule
            val = int(val)
            lo, hi = ranges[key]
            if op == '<':
                if val <= lo:
                    continue
                new_ranges = ranges.copy()
                new_ranges[key] = (lo, min(val - 1, hi))
                result.extend(calcRange(goto, new_ranges, rule_dict))
                ranges[key] = (max(lo, val), hi)
            elif op == ">":
                if val >= hi:
                    continue
                new_ranges = ranges.copy()
                new_ranges[key] = (max(lo, val + 1), hi)
                result.extend(calcRange(goto, new_ranges, rule_dict))
                ranges[key] = (lo, min(val, hi))
    return result


file = open("input.txt")

line = file.readline().strip()
rule_dict = dict()
while line != "":
    key, rules = re.match("(\\w+)\\{([^}]+)}", line).groups()
    for rule in rules.split(","):
        add_in = (rule, )
        if ":" in rule:
            cond, goto = rule.split(":")[:2]
            cond = re.match("([xmas])([<>])(\\d+)", cond).groups()
            add_in = (cond, goto)
        rule_dict.setdefault(key, []).append(add_in)
    line = file.readline().strip()

print(rule_dict)
line = file.readline().strip()

queue = []
start = ("in", {"x": (1, 4000), "m": (1, 4000), "a": (1,4000), "s": (1,4000)})
queue.append(start)
accepted = calcRange("in", start[1], rule_dict)
total = 0
for accept in accepted:
    states = 1
    for lo, hi in accept.values():
        states *= hi - lo + 1
    total += states
print(total)
"""
total = 0
while line != "":
    curr = "in"
    struct = re.match("\\{([^}]+)}", line).group(1)
    obj = dict()
    for pair in struct.split(","):
        key, val = pair.split("=")[:2]
        obj[key] = int(val)
    while curr != 'A' and curr != 'R':
        for rule in rule_dict[curr]:
            if len(rule) == 1:
                curr = rule[0]
                break
            else:
                cond, goto = rule
                if cond[1] == '<' and obj[cond[0]] < int(cond[2]):
                    curr = goto
                    break
                elif cond[1] == '>' and obj[cond[0]] > int(cond[2]):
                    curr = goto
                    break
        print(curr)
    if curr == 'A':
        for val in obj.values():
            total += val
    line = file.readline().strip()
print(total)
"""