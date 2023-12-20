import math
from collections import defaultdict

file = open("input.txt")

modules = dict()
target = None
for line in file:
    components = line.strip().split()
    key = components[0]
    type = None
    if components[0].startswith("%") or components[0].startswith("&"):
        key = components[0][1:]
        type = components[0][0]
    dests = []
    for dest in components[2:]:
        if dest.endswith(","):
            dests.append(dest[:-1])
        else:
            dests.append(dest)
    modules[key] = (type, dests)
    if "rx" in dests:
        target = key
print(modules)

state = dict()
for key in modules.keys():
    state[key] = (False, dict())
look_for = set()
for key, (type, dests) in modules.items():
    for dest in dests:
        if dest in modules:
            state[dest][1][key] = False
        if dest == target:
            look_for.add(key)

print(state)
print(look_for)
seens = defaultdict(list)
for i in range(1000000):
    print(seens)
    queue = [("broadcaster", False, "button")]
    if len(seens) == len(look_for) and all(len(val) == 2 for val in seens.values()):
        cycles = []
        for val in seens.values():
            cycles.append(val[1] - val[0])
        print(math.lcm(*cycles))
        break
    while queue:
        node, signal, source = queue.pop(0)
        if node not in modules:
            continue
        if source in look_for and signal:
            seens[source].append(i + 1)
        if node == 'rx' and not signal:
            print(i+1)
            exit(0)
        type, nexts = modules[node]
        curr_sig, last_seen = state[node]
        if type is None:
            for next in nexts:
                queue.append((next, state[node][0], node))
        elif type == "%":
            if not signal:
                state[node] = (not curr_sig, last_seen)
                for next in nexts:
                    queue.append((next, state[node][0], node))
        elif type == "&":
            state[node][1][source] = signal
            all_true = True
            for val in last_seen.values():
                all_true = all_true & val
            state[node] = (not all_true, last_seen)
            for next in nexts:
                queue.append((next, state[node][0], node))